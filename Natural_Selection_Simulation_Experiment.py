def Natural_Selection_Simulation_Experiment():
    import random
    import math
    import matplotlib.pyplot as plt
    import numpy as np
    E = [1, 1]
    A = [[1, 1] for x in range(10)]
    pop_sizes = []
    rang = []
    n = 15
    Es = [[], []]
    for x in range(n):
        rang.append(x)
        E[0] += random.uniform(0, 1)
        E[1] += random.uniform(0, 1)
        if abs(E[0] - 5) >= 5 or abs(E[1] - 5) >= 5:
            while abs(E[0] - 5) >= 5 or abs(E[1] - 5) >= 5:
                E[0] += random.uniform(0, 1)
                E[1] += random.uniform(0, 1)
        for a in A:
            a[0] += random.uniform(-1, 1)
            a[1] += random.uniform(-1, 1)
            if math.sqrt((a[0] - E[0]) ** 2 + (a[1] - E[0]) ** 2) > 2.5 - 2*len(A)/(len(A)+100) \
                    or abs(a[0] - 5) >= 5 or abs(a[1] - 5) >= 5:
                A =[i for i in A if i !=a]
            else:
                for u in range(2):
                    A.append([a[0],a[1]])
        pop_sizes.append(len(A))
        print(E)
        print(A, "\n")
        def plot():
            X = [ay[0] for ay in A]
            Y = [ay[1] for ay in A]
            plt.scatter(X, Y, c=[0.2,(x)/(n),(x)/(2*n)+0.5],s=5)
            Es[0].append(E[0])
            Es[1].append(E[1])
            #plt.scatter(E[0],E[1],c='black',s=5)
            plt.xlim(0, 10)
            plt.ylim(0, 10)
            plt.xlabel("Trait A")
            plt.ylabel("Trait B")
            #plt.legend("A","B")
            plt.suptitle('Evolution of traits A and B of population through generations represented by colour')
            #plt.show()
        plot()
    print(Es)
    plt.plot(Es[0], Es[1], 'o--', color='black',markersize=5, label="Optimal Traits for Survival")
    plt.plot(Es[0][0], Es[1][0], 's', color='black',markersize=15, label = "Initial Optimal Balance of Traits")
    plt.plot(Es[0][-1],Es[1][-1], 'X', color='black', markersize=15, label = "Final Optimal Balance of Traits")
    plt.legend()
    plt.show()
    print("\n", pop_sizes)
    plt.plot(rang, pop_sizes, 'o--')
    plt.xlabel("Number of Generations")
    plt.ylabel("Population")
    plt.suptitle('Population vs Generations')
    plt.show()
    print(np.random.rand(3,))

Natural_Selection_Simulation_Experiment()


