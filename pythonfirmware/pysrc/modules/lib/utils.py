import time as utime


def convertUint8ToInt8(v, size=8):
    """ Convert variable length uint blocks to int, defaults to 8 bit blocks/bytes
    """
    if v & (0b1 << (size-1)):
        return v - (0b1 << size)
    else:
        return v


def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]

    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(myname, delta/1000))
        return result
    return new_func
