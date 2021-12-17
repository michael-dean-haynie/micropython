def post_readings():
    import socket

    # setup socket connection
    addr = socket.getaddrinfo('codetudes.com', 80)[0][-1]
    print(str(addr))
    s = socket.socket()
    s.setblocking(False)
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
    s.send(bytes(http_msg, 'utf8'))
    print('starting to receive on socket')
    while True:
        data = s.recv(1024)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    print('done receiving on socket')
    s.close()


##############################################################################
# post_readings()

import machine
import time


# setup analog pin
adc = machine.ADC(0)
prev_reading = None

def get_ms_elapsed(start):
    return time.ticks_diff(time.ticks_ms(), start)

start = time.ticks_ms() # get millisecond counter
ms_elapsed = get_ms_elapsed(start)

while(True):
    ms_elapsed = get_ms_elapsed(start)
    new_reading = adc.read()

    # print reading if it's changed
    if (new_reading != prev_reading):
        prev_reading = new_reading
        print(str(prev_reading) + ' ' + '='*prev_reading)
        post_readings()

    # ctrl + c to break out of loop


