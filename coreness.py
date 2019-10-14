import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import json
removed_node = set()
G = nx.Graph()
def coreness():
    n = 0
    core = dict()
    edge = G.edges._graph.edges.__len__()
    while(edge>0):
        nstr = str(n)
        core[nstr] = []
        flag = 1
        while flag == 1:
            flag = 0
            all_nodes = list(G.node)
            all_degree = list(nx.degree(G))
            removed_list = []
            for i in range(len(all_nodes)):
                if all_degree[i][1] <= n:
                    removed_list.append(i)
                    flag = 1
            for i in removed_list:
                G.remove_node(all_nodes[i])
                core[nstr].append(all_nodes[i])
        print(str(n) + "core")
        print(nx.degree(G))
        nx.draw(G, node_size=30, with_labels=False)
        plt.show()
        n += 1
        edge = G.edges._graph.edges.__len__()
    return core

if __name__=='__main__':
    with open('COMPLEX/add_edge.json', "r") as c:
        dm = json.load(c)
        add_i = dm['i']
        add_j = dm['j']
    with open('matrix(7).txt', "r") as f:
        matrix = np.loadtxt(f)
    m_shape = np.array(matrix).shape
    lenss = m_shape[0]
    nodes = list(range(lenss))
    G.add_nodes_from(nodes)
    edge = 0
    for i in range(lenss):
        for j in range(lenss):
            if (matrix[i][j] == 1):
                G.add_edge(i, j)
                edge += 1

    for i in range(len(add_i)):
        G.add_edge(add_i[i], add_j[i])
        G.add_edge(add_j[i], add_i[i])
        edge += 1
    nx.draw(G, node_size=30, with_labels=False)
    hist = nx.degree_histogram(G)
    plt.show()
    record_coreness = coreness()
    coreness_map = {}
    for i in record_coreness:
        for j in record_coreness[i]:
            coreness_map[j] = i

    path = 'G:\complexnetwork\src1\src1'
    file = []
    file_map = {}
    import os
    index = 0
    for i in os.listdir(path):
        file.append(i.split(".")[0])
        file_map[i.split(".")[0]] = index
        index += 1
    index = 0
    for i in file:
        jsname = path + "\\" + i + '.json'
        with open(jsname, "r", errors='ignore', encoding='utf-8') as f:
            jsfile = f.read()
            load_dict = json.loads(jsfile)
            load_dict['coreness'] = coreness_map[file_map[i]]
            index += 1

        with open('src2\\src2\\' + i + '.json', "w") as wf:
            json.dump(load_dict, wf)