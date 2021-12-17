import machine
import time

# setup analog pin
adc = machine.ADC(0)
prev_reading = None

def get_ms_elapsed(start):
    return time.ticks_diff(time.ticks_ms(), start)

start = time.ticks_ms() # get millisecond counter
ms_elapsed = get_ms_elapsed(start)

print('starting loop')
while(True):
    ms_elapsed = get_ms_elapsed(start)
    new_reading = adc.read()

    # print reading if it's changed
    if (new_reading != prev_reading):
        prev_reading = new_reading
        print('='*prev_reading)

print('loop finished')
# ctrl + c to break out of loop 
