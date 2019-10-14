import numpy as np
import json

with open('matrix(7).txt', "r") as f:
    G = np.loadtxt(f, dtype=np.int)
m_shape = np.array(G).shape
l = m_shape[0]

add_edge_i = []
add_edge_j = []
for j in range(1, l):
    if G[j][j - 1] == 0:
        add_edge_i.append(j)
        add_edge_j.append(j-1)

in_json = {}
in_json['i'] = add_edge_i
in_json['j'] = add_edge_j

with open('COMPLEX/adds.json', "w") as f:
    json.dump(in_json, f)

