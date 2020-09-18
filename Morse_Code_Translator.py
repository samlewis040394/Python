def Morse_Code_Transaltor(code='I did this to solve a bletchley park puzzle'):
    import string
    import array as arr
    import numpy
    import itertools
    # import enchant
    Code = code
    arr = numpy.empty((4, 4), dtype=object)
    arr[0, 0] = "hi"
    alphabet = list(string.ascii_lowercase)
    for x in range(10):
        alphabet.append(str(x))
    # d = enchant.Dict("en_US")
    # d.check("hat")
    Morset = [["a", "o-"], ["b", "-ooo"], ["c", "-o-o"], ["d", "-oo"], ["e", "o"], ["f", "oo-o"], ["g", "--o"],
              ["h", "oooo"], ["i", "oo"], ["j", "o---"], \
              ["k", "-o-"], ["l", "o-oo"], ["m", "--"], ["n", "-o"], ["o", "---"], ["p", "o--o"], ["q", "--o-"],
              ["r", "o-o"], ["s", "ooo"], ["t", "-"], \
              ["u", "oo-"], ["v", "ooo-"], ["w", "o--"], ["x", "-oo-"], ["y", "-o--"], ["z", "--oo"], ["0", "-----"],
              ["1", "o----"], ["2", "oo---"], ["3", "ooo--"], \
              ["4", "oooo-"], ["5", "ooooo"], ["6", "-oooo"], ["7", "--ooo"], ["8", "---oo"], ["9", "----o"],
              [" ", "/"]]

    morsset = list()
    for char in Code:
        for x in range(len(Morset)):
            if char in Morset[x][0]:
                morsset.append(Morset[x][1])
    print(" ".join(morsset))

Morse_Code_Transaltor('Some other text')


