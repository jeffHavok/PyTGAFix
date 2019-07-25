from tkinter import *
from tkinter.filedialog import askopenfilename
from common import *

root = Tk()

Tk().withdraw()
fName = askopenfilename()
img = readTGA(fName)
print(img.conf)
vH = 512
vW = 512
Zoom = 1
if (img.conf['H'] <= 512 and img.conf['W'] <= img.conf['H']):
    Zoom = int(512 / img.conf['H'])
if (img.conf['W'] <= 512 and img.conf['H'] <= img.conf['W']):
    Zoom = int(512 / img.conf['W'])
if img.conf['H'] > 512:
    W = img.conf['W']
    H = img.conf['H']

c = Canvas(root, width=512, height=512, bg='white')
c.pack()

for j in range(0, img.conf['W']):
    for i in range(0, img.conf['H']):
        #print("i: " + str(i) + " j: " + str(j))
        tempCh = hex(img.C[img.data[i][j]])[2:].zfill(6)
        print(str(img.data[i][j]) + "   hex:#" + str(tempCh))
        tempC = "#" + str(tempCh)
        c.create_rectangle(i*Zoom,
                           j*Zoom,
                           i*Zoom+Zoom,
                           j*Zoom+Zoom,
                           fill=tempC, outline="")

root.mainloop()
