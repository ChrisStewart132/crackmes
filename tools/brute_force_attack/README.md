# BRUTE FORCE ATTACK
simulation of a brute force attack using multi processing 
implemented with a python command script and with both python and C test servers and subprocesses

# Example Use
step 1: configure the test server password (defined in testServer.py/c)
step 2: configure password length, symbols, and number of cores to use in the bruteForcing.py script
step 3: run the testServer (e.g. using the .bat file or compiling and running yourself if not on windows)
step 4: run the bruteForcing.py script which will automatically create sub processes depending on how many cores were specified
step 5: wait for the test server to report a succesful password guess

with 4 cores, a decimal password of length 8 (23622295), and a test server implemented in C
	(note the first 4 cores/subprocesses start from 1,2,3,4 respectively, so core 2 will succeed with (23622295))
	C: 226s
	py: 210s