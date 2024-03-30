import socket
HOST, PORT = "127.0.0.1", 10487
PASSWORD = "2362339"
N = 10**len(PASSWORD)
INVALID_MESSAGE = "IM"
VALID_MESSAGE = "success"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
i = 0
cache = {}
while True:
    data, addr = s.recvfrom(64)
    if addr[1] in cache:
        cache[addr[1]] += 1
    else:
        cache[addr[1]] = 1
    i+=1
    if i%1000000 == 0:
        print(i, [cache[i]/N for i in cache.keys()])
    response = INVALID_MESSAGE
    if data.decode("utf-8") == PASSWORD:
        response = VALID_MESSAGE
        print(data, addr, response)
    s.sendto(response.encode("utf-8"), addr)
