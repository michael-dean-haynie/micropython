def post_readings():
    import socket
    addr = socket.getaddrinfo('codetudes.com', 80)[0][-1]
    print(str(addr))
    s = socket.socket()
    s.connect(addr)
    http_msg = """POST /readings HTTP/1.1
Host: codetudes.com
Content-Type: application/json
Content-Length: 189

[
    {
        "msOffset": 291,
        "magnitude": 501
    },
    {
        "msOffset": 500,
        "magnitude": 27
    },
    {
        "msOffset": 18,
        "magnitude": 121
    }
]"""
    # s.send(bytes('POST /readings HTTP/1.1\nHost: codetudes.com\nContent-Type: application/json\n\n[{"msOffset":100,"magnitude":500}]', 'utf8'))
    s.send(bytes(http_msg, 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()


post_readings()