import time

def log_something(ms_elapsed):
    print('time elapsed in ms: ' + str(ms_elapsed))

def log_something_else(delay):
    print('delay in ms: ' + str(delay))

def get_ms_elapsed(start):
    return time.ticks_diff(time.ticks_ms(), start)


start = time.ticks_ms() # get millisecond counter
ms_elapsed = get_ms_elapsed(start)

while(ms_elapsed < 500):
    old_ms_elapsed = ms_elapsed
    ms_elapsed = get_ms_elapsed(start)
    log_something(ms_elapsed)
    log_something_else(ms_elapsed - old_ms_elapsed)