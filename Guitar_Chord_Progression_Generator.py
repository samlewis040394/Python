def Guitar_Chord_Progression_Generator():
    import random
    import webbrowser

    # Lists representing music theory data
    steps = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    notes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B",)
    symbolsteps = ("1", "b9", "2", "#9", "3", "4", "b5", "5", "#5", "6", "b7", "7")
    altsymbolsteps = (" ", " ", "9", "b3", " ", "11", "#11", " ", " ", "13", "", " ")
    chords = list()
    chordssteps = list()
    notesinchords = list()
    allmajorscales = list()

    # Reading text file containing chord data from http://www.all-guitar-chords.com/
    # and adding to music theory data lists above
    f = open("Guitar_Chord_Progression_Generator.txt", "r")
    for i, line in enumerate(f):
        if "Symbols:" in line:
            chords.append(line[line.index(":") + 2:len(line) - 1])
        if "Steps:" in line:
            chordssteps.append(line[line.index(":") + 2:len(line) - 1])

    # Creating scale choice
    for x in range(12):
        majorscales = [x, x + 2, x + 4, x + 5, x + 7, x + 9, x + 11]
        for z in range(3):
            for y in majorscales:
                if y > 11:
                    majorscales.remove(y)
                    majorscales.append(y - 12)
        majorscales.sort()
        allmajorscales.append(majorscales)
    print(allmajorscales)

    # Generating valid chords from notes of specified scale
    while True:
        notesinchords = list()
        chordprog = list()
        for e in range(4):
            chordnote = notes[random.randint(0, len(notes) - 1)]
            chordclass = chords[random.randint(0, len(chords) - 1)]
            chordsteps = chordssteps[chords.index(chordclass)]
            chordname = chordnote + " " + chordclass
            chordprog.append(chordname)
            print(chordname)
            print(chordsteps)
            z = chordsteps.split("-")
            chordnotes = list()
            for x in range(len(chordsteps.split("-"))):
                if z[x] in symbolsteps:
                    if notes.index(chordnote) + symbolsteps.index(z[x]) < 12:
                        chordnotes.append(notes[notes.index(chordnote) + symbolsteps.index(z[x])])
                    if notes.index(chordnote) + symbolsteps.index(z[x]) > 11:
                        chordnotes.append(notes[notes.index(chordnote) + symbolsteps.index(z[x]) - 12])
                if z[x] in altsymbolsteps:
                    if notes.index(chordnote) + altsymbolsteps.index(z[x]) < 12:
                        chordnotes.append(notes[notes.index(chordnote) + altsymbolsteps.index(z[x])])
                    if notes.index(chordnote) + altsymbolsteps.index(z[x]) > 11:
                        chordnotes.append(notes[notes.index(chordnote) + altsymbolsteps.index(z[x]) - 12])
            print(chordnotes)
            for c in range(len(chordnotes)):
                if notes.index(chordnotes[c]) not in notesinchords:
                    notesinchords.append(notes.index(chordnotes[c]))
        notesinchords.sort()
        print(notesinchords)
        if notesinchords in allmajorscales:
            print(chordprog)
            break

    # Opening valid tabs on http://www.all-guitar-chords.com/ containing valid chords
    for x in range(len(chordprog)):
        if "#" in chordprog[x].split(" ")[0] or "#" in chordprog[x].split(" ")[1]:
            if "#" in chordprog[x].split(" ")[1] and "#" in chordprog[x].split(" ")[0]:
                webbrowser.open(
                    "http://www.all-guitar-chords.com/index.php?ch=" + chordprog[x].split(" ")[0][0] + "%23%2F" +
                    notes[notes.index(chordprog[x].split(" ")[0][0]) + 2][0] + "b" + "&mm=" +
                    (chordprog[1].split(" ")[1].split("#"))[0] + "%23"
                    + (chordprog[1].split(" ")[1].split("#"))[1] + "" + "&get=Get")
            else:
                if "#" in chordprog[x].split(" ")[0]:
                    webbrowser.open(
                        "http://www.all-guitar-chords.com/index.php?ch=" + chordprog[x].split(" ")[0][0] + "%23%2F" +
                        notes[notes.index(chordprog[x].split(" ")[0][0]) + 2][0] + "b" + "&mm=" +
                        chordprog[x].split(" ")[
                            1] + "&get=Get")
                else:
                    webbrowser.open(
                        "http://www.all-guitar-chords.com/index.php?ch=" + chordprog[x].split(" ")[0] + "&mm=" +
                        (chordprog[1].split(" ")[1].split("#"))[0] + "%23"
                        + (chordprog[1].split(" ")[1].split("#"))[1] + "&get=Get")
        else:
            webbrowser.open("http://www.all-guitar-chords.com/index.php?ch=" + chordprog[x].split(" ")[0] + "&mm=" +
                            chordprog[x].split(" ")[1] + "&get=Get")


Guitar_Chord_Progression_Generator()



