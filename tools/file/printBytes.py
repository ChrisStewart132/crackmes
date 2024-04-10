import sys

# arg usage checking
if len(sys.argv) < 2:
    print(sys.argv[0] + " usage: FILE_PATH")
    exit(1)

# process args
FILE_PATH = sys.argv[1]
print(f"FILE_PATH: {FILE_PATH}")

def print_bytes(file_path):
    with open(file_path, 'rb') as file:
        row = 0
        while True:
            chunk = file.read(16)  # Read 8 bytes at a time
            if not chunk:  # If end of file is reached, break the loop
                break
            hex_bytes = ' '.join([f'{byte:02X}' for byte in chunk])  # Convert bytes to hexadecimal
            ascii_chars = ''.join([chr(byte) if 32 <= byte <= 126 else '.' for byte in chunk])  # Convert printable ASCII bytes to characters
            print(f'0x{row:08X}: {hex_bytes.ljust(24)}' + ' '*8 + f'{ascii_chars}')
            row+=1
            if row % 32 == 0:
                input("continue:")

if __name__ == "__main__":
    print_bytes(FILE_PATH)
