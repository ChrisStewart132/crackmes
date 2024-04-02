import subprocess
import os
import time

# define some common symbol strings
binary = "01"
decimal = "0123456789"
hexadecimal = decimal + "ABCDEF"
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = lower_case.upper()
alphabet = lower_case + upper_case

# 0=python, 1=C
MODE = 0
# largest possible length to try
MAX_PASSWORD_LENGTH = 8
# alphabet to be used
SYMBOLS = decimal
N_CORES = 4

def dfs_backtrack(output, is_solution, add_to_output, children, candidate=""):
    """
        output: container solutions are added to
        is_solution: boolean function, true if candidate is a solution
        add_to_output: function that adds the input candidate to the output container
        children: function that returns child nodes/variant of the given node/candidate
    """
    if is_solution(candidate):
        add_to_output(candidate, output)
    else:
        for child_candidate in children(candidate):
            dfs_backtrack(output, is_solution, add_to_output, children, child_candidate)

def variations(desired_length, symbols=['a','b','c'], starting_candidate=""):
    """
    Variations is a selection of any number of each item and in any order
        n=size of set, k=desired_length
        V = n**k
    """
    def is_solution(candidate):
        return len(candidate) == desired_length
    def add_to_output(candidate, output):
        output.append(candidate)
    def children(candidate):     
        return [candidate + str(x) for x in symbols]
    solutions = []
    dfs_backtrack(solutions, is_solution, add_to_output, children, starting_candidate)
    return solutions
    
def generate_first_candidates(characters, n_candidates):
    if n_candidates <= len(characters):
        return [char for char in characters]
    else:
        # n_candidates = n_characters**length
        length = 1
        while len(characters)**length < n_candidates:
            length+=1
        return variations(length, characters)


# generate the starting candidates for parallel processing
first_candidates = generate_first_candidates(SYMBOLS, N_CORES)

processes = []
# check the search space prior to the starting candidates
if len(first_candidates[0]) > 1:
    if MODE == 0:
        processes.append(subprocess.Popen(['python', 'bruteForcingSubProcess.py', str(len(first_candidates[0])-1), SYMBOLS, "", str(os.getpid())]))
    else:
        processes.append(subprocess.Popen(['./bruteForcingSubProcess.exe', str(len(first_candidates[0])-1), SYMBOLS, ""]))

for candidate in first_candidates:
    if len(processes) >= N_CORES:
        processes[0].wait()
        process = processes.pop(0)
        print(f"Subprocess {process.pid} completed.")
    if MODE == 0:
        process = subprocess.Popen(['python', 'bruteForcingSubProcess.py', str(MAX_PASSWORD_LENGTH), SYMBOLS, candidate, str(os.getpid())])
    else:
        process = subprocess.Popen(['./bruteForcingSubProcess.exe', str(MAX_PASSWORD_LENGTH), SYMBOLS, candidate])
    time.sleep(0.2)
    processes.append(process)
    print(candidate, processes[-1].pid)

for process in processes:
    process.wait()
    #print(f"Subprocess {process.pid} completed.")
