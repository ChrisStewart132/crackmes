import os
import sys

# arg usage checking
if len(sys.argv) < 2:
    print(sys.argv[0] + " usage: FILE_PATH OVERWRITE_CHAR=33")
    exit(1)

# process args
FILE_PATH = sys.argv[1]
OVERWRITE_CHAR = 33 if len(sys.argv) == 2 else (int(sys.argv[2])%256)
print(f"FILE_PATH:{FILE_PATH}, OVERWRITE_CHAR:{chr(OVERWRITE_CHAR)}")

# check the path is valid
if not os.path.isfile(FILE_PATH):
    print("invalid path.")
    exit(1)

# read the file 
file = open(FILE_PATH, 'rb')
file_data = file.read()
nBytes = len(file_data)
file.close()

# overwrite the file
file = open(FILE_PATH, 'wb')
file.write(bytes([OVERWRITE_CHAR]*nBytes))
file.close()