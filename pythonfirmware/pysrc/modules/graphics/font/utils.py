
from utils import timed_function, traced_function


def convertUint8ToInt8(v, size=8):
    """ Convert variable length uint blocks to int, defaults to 8 bit blocks/bytes
    """
    if v & (0b1 << (size-1)):
        return v - (0b1 << size)
    else:
        return v


def read_word_from_bytes(bytes, pos):
    d = bytes[pos]
    d <<= 8
    d += bytes[pos+1]
    return d


class BitstreamReader:
    def __init__(self, data, offset: uint = 0):
        self.data = data
        self.move_to(offset)

    def move_to(self, offset: uint):
        self.bytePos = offset//8
        self.bitPos = offset % 8

    def read_unsigned_bits(self, cnt: uint) -> uint:
        bpos = self.bitPos
        pos = self.bytePos

        bposFinal = bpos+cnt
        v = 0

        if bposFinal < 8:
            v = self.data[pos]
            v >>= bpos
            v &= (1 << cnt)-1
        else:
            v = self.data[pos]
            pos += 1
            v += self.data[pos] << 8
            v >>= bpos
            v &= (1 << cnt)-1

        bpos = bposFinal % 8
        self.bytePos = pos
        self.bitPos = bpos
        return v

    def read_signed_bits(self, cnt):
        v = self.read_unsigned_bits(cnt)
        d = 1
        cnt -= 1
        d <<= cnt
        v -= d
        return v


class PixelPointer:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height

    def step_y(self, reset_x=False):
        self.y += 1
        if reset_x:
            self.x = 0
        return self

    def is_overflow(self) -> bool:
        return self.y >= self.heigth

    def step(self):
        self.x += 1
        if self.x >= self.width:
            self.step_y(True)
