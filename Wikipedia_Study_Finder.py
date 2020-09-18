def findstudiesfromnwikiurls(n,url):
    import random
    import requests as req
    import re
    for b in range(n):
        resp = req.get(url)
        content = resp.text
        k = open("guru99.txt", "w+")
        k.write(content)
        k = open("guru99.txt", "r")
        topics = list()
        for i, line in enumerate(k):
            split = (re.sub('<[^<]+?>', '', line)).split(".",0)
            if "<a href=\"/wiki/" in line and ":" not in line:
                link = str(line)[line.index("<a href=\"/wiki/") + len("<a href=\"/wiki/"):len(line)]
                linke = link[0:link.index("\"")]
                topics.append(linke)
                # print(linke + "\n")
            if "<p>" in line and "^" not in line:
                words = [" studies ", "Studies ", "Study ", " study", "research"]
                words2 = [" found ", " show ", " display ", " demonstrate ", " conclu"]
                words3 = ["emotion", "intelligen", "happiness", "well-being", "clarity", "love", "mental", "feeling", "euphoria"]
                if any(words[y] in line for y in range(len(words))) is True:
                    for x in range(len(split)):
                        for letter in set(";1234567890&#"):
                            if letter in split[x]:
                                split.insert(x+1, split[x].replace(letter, ""))
                                split.remove(split[x])
                        if any(words[y] in split[x] for y in range(len(words))) is True and \
                                any(words2[y] in split[x] for y in range(len(words2))) is True and \
                                any(words3[y] in split[x] for y in range(len(words3))) is True:
                             if split[x][0].isupper() is True or split[x][1].isupper() is True:
                                     if len(str(split[x])) < 1000:
                                         print(split[x][0:len(split[x])] + "\n")
        topic = topics[random.randint(0, len(topics) - 1)]
        url = "https://en.wikipedia.org/wiki/" + topic
        #print(url)

findstudiesfromnwikiurls(10,"https://en.wikipedia.org/wiki/Code")