def Risk():
    Risk = {}
    Colors = {'North America': 'yellow', 'South America': 'red', 'Europe': 'blue', 'Africa': 'orange', 'Asia': 'green',
              'Oceania': 'purple'}
    import networkx as nx
    import json
    import matplotlib.pyplot as plt
    #from networkx.drawing.nx_agraph import graphviz_layout
    R = nx.Graph()

    with open('Risk.txt', 'r') as r:
        lines = r.readlines()
        for x in range(1, len(lines)):
            lines[x] = lines[x].split("\n")[0]
            if lines[x - 1] == '':
                Cont = lines[x]
                Risk[lines[x]] = []
            elif x != 1 and lines[x] != '':
                Risk[Cont].append(lines[x])
        # print(Risk)

    Countries = [x for cont in Risk.values() for x in cont]
    # print(Countries)
    colour_map = []
    for a in Countries:
        R.add_node(a)
        Coont = [n[0] for n in Risk.items() if a in n[1]][0]
        colour_map.append(Colors[Coont])

    with open('Connections.txt', 'r') as rr:
        lines = rr.readlines()[0]
        json_acceptable_string = lines.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        for a in Countries:
            for cun in d[a]:
                R.add_edge(cun, a)

    uniq = list(set(R.nodes()))
    for node in uniq:
        if node not in Countries:
            R.remove_node(node)
    pos = nx.spring_layout(R)
    #nx.draw_networkx(R,pos=pos, node_color=colour_map)
    nx.draw_networkx(nx.bfs_tree(R,'Iceland'),pos=pos)
    plt.show()
Risk()