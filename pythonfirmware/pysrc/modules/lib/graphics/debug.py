def dump_buffer(buf, w, h):
    line = ""
    for y in range(h):
        for x in range(w):
            if (x == 0):
                line = "{:2d}".format(y)
            if (buf.pixel(x, y)):
                line += "O"
            else:
                line += "."
        print(line)
