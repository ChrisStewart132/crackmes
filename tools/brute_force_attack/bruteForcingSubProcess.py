import signal
import sys
import os
import time
import socket

HOST, PORT = "127.0.0.1", 10487
S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
START_TIME = time.time()
ARGS = sys.argv
if len(ARGS) == 3:
    ARGS.append("")
elif len(ARGS) == 4:
    pass
elif len(ARGS) != 5:
    print("usage: [max_length_int, symbols_string, opt:candidate_string, opt:parentPid]")
    sys.exit(1)

def test_candidate(candidate):
    S.sendto(candidate.encode("utf-8"), (HOST, PORT))
    response = S.recv(64)
    if response.decode("utf-8") == "success":
        return True
    return False

def brute_force_iterative(max_length, symbols, candidate=""):
    stack = [candidate]
    while len(stack) > 0:
        candidate = stack.pop()
        # test the candidate
        if test_candidate(candidate):
            print(f"candidate:{candidate} pid:{os.getpid()} port:{PORT} t:{time.time() - START_TIME:.2F}s")
            if len(ARGS) == 5:# send signal to parent 
                os.kill(int(ARGS[4]), signal.SIGTERM)
            exit(0)
        # test the candidates children if applicable
        if len(candidate) < max_length:
            children = [candidate + str(x) for x in symbols]
            for child in children:
                stack.append(child)

brute_force_iterative(int(ARGS[1]), [str(x) for x in ARGS[2]], ARGS[3])