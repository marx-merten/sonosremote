def dump_buffer(buf, w, h, char_blk='O', char_white='.'):
    line = ""
    for y in range(h):
        for x in range(w):
            if (x == 0):
                line = "{:2d}: ".format(y)
            if (buf.pixel(x, y)):
                line += char_white
            else:
                line += char_blk
        print(line)
