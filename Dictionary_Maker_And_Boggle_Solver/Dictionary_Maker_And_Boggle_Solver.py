def dictionarymaker():
    import urllib.request
    import string
    fulldict = list()
    alphabet = list(string.ascii_lowercase)
    for x in range(len(alphabet)):
        for y in range(100):
            try:
                resource = urllib.request.urlopen('https://www.dictionary.com/list/' + alphabet[x] + '/' + str(y))
                from html.parser import HTMLParser
                class HTMLFilter(HTMLParser):
                    text = ""

                    def handle_data(self, data):
                        self.text += data

                f = HTMLFilter()
                f.feed(str(resource.read()))
                p = f.text.split("\"displayForm\":\"")
                for elem in p:
                    if "\",\"url\":\"" in elem:
                        if "\\" in elem:
                            None
                        else:
                            word = elem.split("\",\"url\":\"")[0].split(" ") \
                                [0].split(".")[0].split("-")[0]
                            if word not in fulldict:
                                fulldict.append(word)
                                d = open('Dictionary.txt', 'a')
                                d.write(word + "\n")
                                print(word)
                            else:
                                None
            except:
                None

    print(fulldict)
    print(alphabet)

def BoggleSolver(rand=True):
    import numpy as np
    import string
    import random
    alphabet = list(string.ascii_lowercase)
    a = np.array([['h', 'e', 'l', 'l'], ['s', 'n', 'i', 'k'], ['p', 'l', 'c', 't'], ['p', 'l', 'a', 't']])
    vowels = ['a', 'e', 'i', 'o', 'u']
    def randboggle():
        for x in range(4):
            for y in range(4):
                a[x, y] = alphabet[random.randint(0, len(alphabet) - 1)]
        for x in range(3):
            a[random.randint(0,3),random.randint(0,3)] = vowels[random.randint(0,4)]
    def inputboggle():
        z = 0
        for x in range(4):
            for y in range(4):
                z = z + 1
                a[x, y] = input("Letter Number " + str(z) + "?")
    if rand == True:
        randboggle()
    else:
        inputboggle()
    #print(a)
    word = list()
    for x in range(4):
        for y in range(4):
            word.append(a[x, y])
    Words = list()
    g = open('Dictionary.txt', 'r')
    for line in g:
        if any(elem in line for elem in vowels):
            if len(line) > 5:
                line = line.split("\n")[0]
                li = list()
                path = list()
                for x in range(len(line)):
                    li.append(line[x])
                    # print(np.where(a == line[x]))
                if all(elem in word for elem in li):
                    if all(word.count(elem) >= li.count(elem) for elem in li):
                        # print(line)
                        for x in range(len(line)):
                            where = np.where(a == line[x])
                            # print(where)
                            sub = list()
                            if len(where[0]) < 2:
                                sub.append([where[0][0], where[1][0]])
                            else:
                                for f in range(len(where[0])):
                                    sub.append([where[0][f], where[1][f]])
                            path.append(sub)
                if path != []:
                    # print(path)
                    val = list()
                    for y in range(2):
                        for z in range(2):
                            val = list()
                            for x in range(len(path)):
                                if len(path[x]) > 1:
                                    val.append(path[x][y])
                                    y = z
                                else:
                                    val.append(path[x][0])
                            # print("\n")
                            # print(val)
                            q = 0
                            for y in range(2):
                                for x in range(len(val) - 1):
                                    if abs(val[x][y] - val[x + 1][y]) < 2:
                                        q = q + 1
                            if q == 2 * (len(val) - 1):
                                if all(val.count(elem) < 2 for elem in val):
                                    print("Word:" + line)
                                    #Words.append(line)
                                    b = np.array([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
                                                  [' ', ' ', ' ', ' ']])
                                    for x in range(len(val)):
                                        b[val[x][0], val[x][1]] = str(x + 1)
                                    print(a)
                                    print("Path:")
                                    print(b)
                                    print("\n")
    for elem in Words:
        if Words.count(elem) == 1:
            None
        else:
            for y in range(Words.count(elem)-1):
                Words.remove(elem)
    for x in range(len(Words)):
        print(Words[x])

BoggleSolver(rand=True)


























