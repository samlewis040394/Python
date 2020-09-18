# Produces fret information for major scales
def scale(root='C',show=False):
    let = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    maj = [0, 1, 3, 5, 7, 8, 10]
    x_maj = sorted([(x + let.index(root)) % 12 for x in maj])
    scale = []
    for y in range(0, 6):
        s = sorted([(x + (7 * y)) % 12 for x in x_maj])
        scale.append(s)
    if show == True:
        print("Guitar frets for the scale {}:".format(root))
        for x in range(len(scale)):
            print("Frets for string {} = {}".format(x + 1, scale[x]))
        print("\n")
    return scale

# Produces fret information for unions or intersections of multiple major scales
def multi_scale(scale_list,show=False,how="outer"):
    exp_scale = []
    for x in range(6):
        exp = []
        for rooty in scale_list:
            exp += scale(root=rooty)[x]
        exp_scale.append(exp)
    if how == "outer":
        for x in range(6):
            exp_scale[x] = list(set(exp_scale[x]))
        if show == True:
            print("Guitar frets for the unions of scales {}:".format(scale_list))
            for x in range(len(exp_scale)):
                print("Frets for string {} = {}".format(x + 1, exp_scale[x]))
            print("\n")
    elif how == "inner":
        for x in range(6):
            exp_scale[x] = [n for n in exp_scale[x] if exp_scale[x].count(n) == len(scale_list)]
            exp_scale[x] = list(set(exp_scale[x]))
        if show == True:
            print("Guitar frets for the intersection of scales {}:".format(scale_list))
            for x in range(len(exp_scale)):
                print("Frets for string {} = {}".format(x + 1, exp_scale[x]))
            print("\n")
    else:
        print("ERROR: \"how\" must be \"inner\" or \"outer\"")
    return exp_scale

# Only represent notes capitalised and without sharps
scale(root='D',show=True)
multi_scale(scale_list=['A','C','E'],show=True,how="inner")
multi_scale(scale_list=['Ab','F'],show=True,how="outer")
