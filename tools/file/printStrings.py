import sys

# arg usage checking
if len(sys.argv) < 2:
    print(sys.argv[0] + " usage: FILE_PATH")
    exit(1)

# process args
FILE_PATH = sys.argv[1]
print(f"FILE_PATH: {FILE_PATH}")
MINIMUM_LENGTH = 8
MAX_ROWS = 16

def find_ascii_strings(file_path):
    ascii_strings = []
    with open(file_path, 'rb') as file:
        current_string = b''
        while True:
            byte = file.read(1)
            if not byte:  # If end of file is reached, break the loop
                break
            
            if 32 <= ord(byte) <= 126:  # Check if byte is within ASCII range
                current_string += byte
            else:
                if len(current_string) > MINIMUM_LENGTH:  # If current_string is not empty, it forms a valid ASCII string
                    ascii_strings.append(current_string.decode())
                current_string = b''

    return ascii_strings

if __name__ == "__main__":
    ascii_strings = find_ascii_strings(FILE_PATH)
    print()
    row = 0
    for string in ascii_strings:
        print(string)
        row += 1
        if row % MAX_ROWS == 0:
            input(": ")
