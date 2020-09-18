def Random_Nearest_Neighbour_Experiment():
    import pandas as pd
    import random
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    s = []
    for x in range(5):
        coord = []
        for y in range(2):
            up = random.randint(0, 100)
            print(up)
            down = random.randint(up + 20, 200)
            print(down)
            rang = [x for x in range(up, down)]
            a = random.sample(rang, 20)
            coord.append(a)
        s.append(coord)
    print(s)

    plt.figure()
    sampy = [[x, y] for x in range(0, 200, 10) for y in range(0, 200, 10)]

    coorddist = []
    colur = []
    for z in range(len(s)):
        # col = np.random.rand(3,)
        col = [random.uniform(0.0, 1.0) for x in range(3)]
        plt.scatter(s[z][0], s[z][1], c='black', s=10)
        for g in range(len(s[z][0])):
            coorddist.append([s[z][0][g], s[z][1][g]])
            colur.append(col)

    for m in range(len(sampy)):
        close = []
        samp = sampy[m]
        for c in range(len(coorddist)):
            close.append(math.sqrt(abs(coorddist[c][0] - samp[0]) ** 2 + abs(coorddist[c][1] - samp[1]) ** 2))
        ind = close.index(min(close))
        coll = colur[ind]
        plt.scatter(samp[0], samp[1], c=coll, s=1000, alpha=0.3)
    plt.show()

Random_Nearest_Neighbour_Experiment()