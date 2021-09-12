def rgb(r, g, b):
    RGB = [r,g,b]
    hex_op = []
    for c in RGB:
        if c>255:
            hex_op.append("FF")
        elif c<0:
            hex_op.append('00')
        elif c in range(0,16):
            hex_op.append("0"+hex(c)[2:].upper())
        else:
            hex_op.append(hex(c)[2:].upper())
    print("".join(hex_op))
rgb(10,2,3)