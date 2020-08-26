# function to alternate pixels of 4 images into one
def imagefuse():
    from PIL import Image
    im1 = Image.open('/Users/g/Downloads/po1.jpg')
    pixelMap1 = im1.load()
    im2 = Image.open('/Users/g/Downloads/po2.jpg')
    pixelMap2 = im2.load()
    im3 = Image.open('/Users/g/Downloads/po6.jpg')
    pixelMap3 = im3.load()
    im4 = Image.open('/Users/g/Downloads/po4.jpg')
    pixelMap4 = im4.load()
    imga = Image.new(im2.mode, (2 * min(im3.size[0], im4.size[0], im1.size[0], im2.size[0]),
                                2 * min(im3.size[1], im4.size[1], im1.size[1], im2.size[1])))
    pixelsNew = imga.load()
    for i in range(imga.size[0]):
        for j in range(imga.size[1]):
            ma = min(im3.size[0], im4.size[0], im1.size[0], im2.size[0])
            mb = min(im3.size[1], im4.size[1], im1.size[1], im2.size[1])
            if j < mb:
                if i < ma:
                    pixelsNew[i, j] = pixelMap2[i, j]
                else:
                    pixelsNew[i, j] = pixelMap1[i - ma, j]
            else:
                if i < ma:
                    pixelsNew[i, j] = pixelMap3[i, j - mb]
                else:
                    pixelsNew[i, j] = pixelMap4[i - ma, j - mb]
    imga.show()
#Modules needed for image processing and restarting system
from PIL import Image
import os
import sys

# Creating Dot Image
imgdot = Image.new("RGB",(150,150),"white")
newpix1 = imgdot.load()
for i in range(imgdot.size[0]):
    for j in range(imgdot.size[1]):
        if (i-75)**2 + (j-75)**2 <= 4000:
            newpix1[i,j] = (0,0,0,200)

# Creating Grid
imgback = Image.new("RGB",(1000,1000),"white")
newpix2 = imgback.load()
for x in range(6):
    for i in range(imgback.size[0]):
        for j in range(imgback.size[1]):
            if (200*x - 5) < i < (200*x + 5):
                newpix2[i, j] = (0, 0, 0, 200)
            if (200*x - 5) < j < (200*x + 5):
                newpix2[i, j] = (0, 0, 0, 200)

# Creating Big White Background to Put Grid on
imgback2 = Image.new("RGB",(1400,1400),"white")
newpix3 = imgback2.load()
for i in range(200,1200):
    for j in range(200,1200):
        newpix3[i,j] = newpix2[i-200,j-200]

# Creating Database with chord name at entry[0]+fretnumber at entry[1]
Chords = [['AMINOR',['X','0','2','2','1','0']] \
,[['AMAJOR'],['X','0','2','2','2','0']] \
,[['BMAJOR'],['X','2','4','4','4','2']] \
,[['BMINOR'],['X','2','4','4','3','2']] \
,[['CMAJOR'],['X','3','2','0','1','0']] \
,[['CMINOR'],['X','3','5','5','4','3']] \
,[['DMAJOR'],['X','X','0','2','3','2']] \
,[['DMINOR'],['X','X','0','2','3','1']] \
,[['EMAJOR'],['0','2','2','1','0','0']] \
,[['EMINOR'],['0','2','2','0','0','0']] \
,[['FMAJOR'],['1','3','3','2','1','1']] \
,[['FMINOR'],['1','3','3','1','1','1']] \
,[['GMAJOR'],['3','2','0','0','3','3']] \
,[['GMINOR'],['3','5','5','3','3','3']]
]

# Input System to pull up fretnumbers from input
chord = input("Chord Name = ").upper()
if any(chord in elem[0] for elem in Chords):
    for elem in Chords:
        if chord in elem[0]:
            print("Chord Exist in Library")
            frets = elem[1]
else:
    print("Chord Doesn't Exist in Library \nTry Again in a few seconds")
    os.execl(sys.executable, sys.executable, *sys.argv)

# Adding dots in right place from fretnumbers to large grid image
for x in range(6):
    if frets[x].isnumeric():
        startx = 125 + (x * 200)
        endx = 275 + (x * 200)
        starty = 25 + (int(frets[x]) * 200)
        endy = 175 + (int(frets[x]) * 200)
        for i in range(startx, endx):
            for j in range(starty, endy):
                newpix3[i, j] = newpix1[i - startx, j - starty]

# Outputting Final Image
imgback2.show()

