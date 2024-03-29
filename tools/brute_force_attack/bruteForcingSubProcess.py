import signal
import sys
import os
import time
START_TIME = time.time()
TEST_PASSWORD = "passwo"
ARGS = sys.argv
if len(ARGS) == 3:
    ARGS.append("")
elif len(ARGS) == 4:
    print("usage: [max_length_int, symbols_string, candidate_string]")
elif len(ARGS) != 5:
    print("usage: [max_length_int, symbols_string, opt:candidate_string, opt:parentPid]")

def brute_force(max_length, symbols, candidate=""):
    # test the candidate
    if candidate == TEST_PASSWORD:
        print(candidate, os.getpid(), F"{time.time() - START_TIME:.2F}s")
        if len(ARGS) == 5:# send signal to parent 
            os.kill(int(ARGS[4]), signal.SIGTERM)
        exit(0)
    # test the candidates children if applicable
    if len(candidate) < max_length:
        children = [candidate + str(x) for x in symbols]
        for child in children:
            brute_force(max_length, symbols, child)

def brute_force_iterative(max_length, symbols, candidate=""):
    stack = [candidate]
    while len(stack) > 0:
        candidate = stack.pop()
        # test the candidate
        if candidate == TEST_PASSWORD:
            print(candidate, os.getpid(), F"{time.time() - START_TIME:.2F}s")
            if len(ARGS) == 5:# send signal to parent 
                os.kill(int(ARGS[4]), signal.SIGTERM)
            exit(0)
        # test the candidates children if applicable
        if len(candidate) < max_length:
            children = [candidate + str(x) for x in symbols]
            for child in children:
                stack.append(child)


#brute_force(int(ARGS[1]), [str(x) for x in ARGS[2]], ARGS[3])
brute_force_iterative(int(ARGS[1]), [str(x) for x in ARGS[2]], ARGS[3])