class TGA(object):
    def __init__(self, conf, C, data):
        self.conf = conf
        self.C = C
        self.data = data


def readTGA(fName):
    img = TGA({}, [0], [])
    with open(fName, "rb") as f:
        def bRead(bSize):
            cont = int.from_bytes(f.read(bSize), byteorder='big', signed=False)
            return int(cont)
        f.read(1)
        img.conf['cPalette'] = (bRead(1) == 1)
        f.read(3)
        img.conf['cPaletteLen'] = bRead(2)
        if img.conf['cPaletteLen'] == 1:
            img.conf['cPaletteLen'] = 255
        img.conf['cPaletteBPP'] = bRead(1)
        f.read(3)
        img.conf['W'] = bRead(2)
        img.conf['H'] = bRead(2)
        img.conf['BPP'] = bRead(2)
        f.read(4)
        for x in range(0, img.conf['cPaletteLen']):
            img.C.append(int.from_bytes(
                f.read(3), byteorder='little', signed=False))

        img.data = [[0] * int(img.conf['W'])
                    for i in range(int(img.conf['W']))]

        for i in range(0, img.conf['H']):
            for j in range(0, img.conf['W']):
                img.data[j][img.conf['H']-i-1] = bRead(1)
        return(img)
