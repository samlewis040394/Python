# Function for inputting into personal association file
def associatefrom(word):
    a = open('Word_Association_Analyser.txt', 'a')
    al = input(word + " > ")
    a.write(word + " > " + al)
    for x in range(10):
        al = input(al+" > ")
        a.write(" > "+al)
    a.write("\n")
    associatefrom(al)
    #a.close()

#Finding associations
def assocfinder(x):
    a = open('Word_Association_Analyser.txt', 'r')
    assoclist = list()
    for line in a:
        if x in line:
            split = line.split("\n")[0].split(" > ")
            #print(split)
            try:
                wordind = split.index(x)
                # print(split)
                # print(wordind)
                if wordind > 0 and wordind < (len(split) - 1):
                    assoclist.append(split[wordind + 1])
                    assoclist.append(split[wordind - 1])
                else:
                    if wordind == 0:
                        assoclist.append(split[wordind + 1])
                    else:
                        assoclist.append(split[wordind - 1])
            except:
                f = 3
    class Format:
        end = '\033[0m'
        underline = '\033[4m'
    print(Format.underline + x.upper() + Format.end)
    #print(x.upper()+" > ")
    finassoc = list()
    newlist = list()
    for elem in assoclist:
        if elem not in finassoc:
            finassoc.append(elem)
            #print(elem + ": "+ str(assoclist.count(elem)))
            newlist.append(elem + ": "+ str(assoclist.count(elem)))
    for x in reversed(range(100)):
        for elem in newlist:
            if str(x) in elem:
                print(elem)
    print("\n")

# Listing associated words and their counts from word association file
def wordlister():
    a = open('Word_Association_Analyser.txt', 'r')
    wordlist = list()
    olist = list()
    orderedlist = list()
    for line in a:
        split = line.split("\n")[0].split(" > ")
        for elem in split:
            wordlist.append(elem)
    for elem in wordlist:
        olist.append(elem+": "+str(wordlist.count(elem)))
    for x in reversed(range(100)):
        for elem in olist:
            if str(x) in elem:
                if elem not in orderedlist:
                    orderedlist.append(elem)
    print(orderedlist)
    for elem in orderedlist:
        assocfinder(elem.split(":")[0])


wordlister()
assocfinder("breath")
associatefrom("word")
