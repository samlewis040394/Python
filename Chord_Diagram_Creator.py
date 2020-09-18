# I have a limited chord library here so see my dictionary (list) below for how to input in
def Chord_Diagram_Creater():
    from PIL import Image
    import sys
    import os
    # Creating Dot Image
    imgdot = Image.new("RGB", (150, 150), "white")
    newpix1 = imgdot.load()
    for i in range(imgdot.size[0]):
        for j in range(imgdot.size[1]):
            if (i - 75) ** 2 + (j - 75) ** 2 <= 4000:
                newpix1[i, j] = (0, 0, 0, 200)

    # Creating Grid
    imgback = Image.new("RGB", (1000, 1000), "white")
    newpix2 = imgback.load()
    for x in range(6):
        for i in range(imgback.size[0]):
            for j in range(imgback.size[1]):
                if (200 * x - 5) < i < (200 * x + 5):
                    newpix2[i, j] = (0, 0, 0, 200)
                if (200 * x - 5) < j < (200 * x + 5):
                    newpix2[i, j] = (0, 0, 0, 200)

    # Creating Big White Background to Put Grid on
    imgback2 = Image.new("RGB", (1400, 1400), "white")
    newpix3 = imgback2.load()
    for i in range(200, 1200):
        for j in range(200, 1200):
            newpix3[i, j] = newpix2[i - 200, j - 200]

    # Creating Database with chord name at entry[0]+fretnumber at entry[1]
    Chords = [['AMINOR', ['X', '0', '2', '2', '1', '0']] \
        , [['AMAJOR'], ['X', '0', '2', '2', '2', '0']] \
        , [['BMAJOR'], ['X', '2', '4', '4', '4', '2']] \
        , [['BMINOR'], ['X', '2', '4', '4', '3', '2']] \
        , [['CMAJOR'], ['X', '3', '2', '0', '1', '0']] \
        , [['CMINOR'], ['X', '3', '5', '5', '4', '3']] \
        , [['DMAJOR'], ['X', 'X', '0', '2', '3', '2']] \
        , [['DMINOR'], ['X', 'X', '0', '2', '3', '1']] \
        , [['EMAJOR'], ['0', '2', '2', '1', '0', '0']] \
        , [['EMINOR'], ['0', '2', '2', '0', '0', '0']] \
        , [['FMAJOR'], ['1', '3', '3', '2', '1', '1']] \
        , [['FMINOR'], ['1', '3', '3', '1', '1', '1']] \
        , [['GMAJOR'], ['3', '2', '0', '0', '3', '3']] \
        , [['GMINOR'], ['3', '5', '5', '3', '3', '3']]
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

Chord_Diagram_Creater()