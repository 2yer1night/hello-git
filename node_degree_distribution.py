import numpy as np
import networkx as nx
import json
removed_node = set()
G = nx.Graph()

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
max_degree = 0
min_degree = 10000000
degree_set = set()
degree_map = {}
for i in list(G.degree):
    if max_degree < i[1]:
        max_degree = i[1]
    if min_degree > i[1]:
        min_degree = i[1]
    if i[1] in degree_set:
        degree_map[i[1]] += 1
    else:
        degree_set.add(i[1])
        degree_map[i[1]] = 1

degree_sorted = sorted(degree_map.items(), key=lambda degree_map:degree_map[0])
degree_json = {}
name = []
value = []
for i in degree_sorted:
    name.append(i[0])
    value.append(i[1])
degree_json['degree'] = json.dumps(name)
degree_json['value'] = json.dumps(value)

with open('COMPLEX/degree.json', "w") as f:
    json.dump(degree_json, f)
