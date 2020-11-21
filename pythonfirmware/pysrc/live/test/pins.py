from globals.pinout import *
from machine import Pin
import utime

sel0 = Pin(SW_SEL0, Pin.OUT)
sel1 = Pin(SW_SEL1, Pin.OUT)
sel2 = Pin(SW_SEL2, Pin.OUT)
in0 = Pin(SW_IN0, Pin.IN)
in1 = Pin(SW_IN1, Pin.IN)
in2 = Pin(SW_IN2, Pin.IN)
in3 = Pin(SW_IN3, Pin.IN)

selectors = [sel2, sel1, sel0]
inputs = [in3, in2, in1, in0]


def read():
    value = 0x00
    for x in selectors:
        x.on()
        for y in inputs:
            value <<= 1
            value += y.value()
        x.off()
    return value


def loop():
    oldv = 0

    while True:
        v = read()
        if v != oldv:
            print("{:020b}".format(v))
            oldv = v
        utime.sleep_ms(20)
