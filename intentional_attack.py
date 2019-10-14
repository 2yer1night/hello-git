import numpy as np
import networkx as nx
import random
import json
removed_node = set()
G = nx.Graph()
save_dict = {}
if __name__=='__main__':
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
    cc = np.empty([lenss, 1], dtype=float)

    e = G.edges._graph.edges.__len__()
    RG = G.copy()
    random_json = []
    random_json.append(lenss)
    RG_e = RG.edges._graph.edges.__len__()
    while RG_e != 0:
        RG_node = list(RG.node)
        count_node = len(RG_node)
        RG.remove_node(RG_node[random.randint(0, count_node)])
        C = nx.connected_component_subgraphs(RG, True)
        g_len = []
        for g in C:
            g_len.append(len(g.node))
        print(max(g_len))
        random_json.append(max(g_len))
        ncc = nx.connected_components(RG)
        nt = []
        for j in ncc:
            if len(j) <= 5:
                for i in j:
                    nt.append(i)
        for i in nt:
            RG.remove_node(i)
            removed_node.add(i)
        RG_e = RG.edges._graph.edges.__len__()

    connect_json = []
    connect_json.append(lenss)
    while e != 0:
        big_node, big_degree = -1, -1
        node_list = list(G.degree)
        for i in node_list:
            if big_degree < i[1]:
                big_node, big_degree = i[0], i[1]
        G.remove_node(big_node)
        removed_node.add(big_node)

        for i in list(G.degree):
            if i[0] not in removed_node and i[1] == 0:
                G.remove_node(i[0])
                removed_node.add(i[0])
        C = nx.connected_component_subgraphs(G, True)
        g_len = []
        for g in C:
            g_len.append(len(g.node))
        # print(max(g_len))
        connect_json.append(max(g_len))
        # nx.draw(G, node_size=30, with_labels=False)
        # hist = nx.degree_histogram(G)
        # plt.show()
        ncc = nx.connected_components(G)
        nt = []
        for j in ncc:
            if len(j) <= 5:
                for i in j:
                    nt.append(i)
        for i in nt:
            G.remove_node(i)
            removed_node.add(i)
        e = G.edges._graph.edges.__len__()

with open('COMPLEX/attack.json', "w") as f:
    in_json = {}
    in_json['intention'] = connect_json
    in_json['random'] = random_json
    json.dump(in_json, f)

