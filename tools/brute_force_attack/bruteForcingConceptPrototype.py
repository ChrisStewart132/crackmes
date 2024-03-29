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

def brute_force(max_length, symbols, output, candidate=""):
    # test if output already found
    if len(output) > 0:
        return
    # test the candidate
    if candidate == "passw":
        output.append(candidate)
        return
    # test the candidates children if applicable
    if len(candidate) < max_length:
        children = [candidate + str(x) for x in symbols]
        for child in children:
            brute_force(max_length, symbols, output, child)
    
def generate_first_candidates(characters, n_candidates):
    if n_candidates <= len(characters):
        return [char for char in characters]
    else:
        # n_candidates = n_characters**length
        length = 1
        while len(characters)**length < n_candidates:
            length+=1
        return variations(length, characters)

# define some common symbols
binary = ['0', '1']
decimal = [str(i) for i in range(10)]
hexadecimal = decimal + list("ABCDEF")
lower_case = list('abcdefghijklmnopqrstuvwxyz')
upper_case = list('abcdefghijklmnopqrstuvwxyz'.upper())
alphabet = lower_case + upper_case

# alphabet to be used
SYMBOLS = lower_case
OUTPUT = []

# generate the starting candidates for parallel processing
N_CORES = 8
first_candidates = generate_first_candidates(SYMBOLS, N_CORES)
print(first_candidates)
n_processes = len(first_candidates)

# check the search space prior to the starting candidates
brute_force(len(first_candidates[0])-1, SYMBOLS, OUTPUT)
print(-1, "", OUTPUT)

# parallel process

# simulation
for i, starting_candidate in enumerate(first_candidates):
    brute_force(5, SYMBOLS, OUTPUT, starting_candidate)
    print(i, starting_candidate, OUTPUT)
















    
