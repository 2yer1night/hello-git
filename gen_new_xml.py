
import os
import xml.etree.ElementTree as ef
import json
import random

# ef.register_namespace('viz', "http://www.gexf.net/1.2draft/viz")
tree = ef.parse('COMPLEX/net.grxf')
root = tree.getroot()
root.set('xmlns', "http://www.gexf.net/1.2draft")
root.set('version', "1.2")
root.set('xmlns:viz', "http://www.gexf.net/1.2draft/viz")
nodes = root[0][1]
edges_ = root[0][2]
# path = 'G:\complexnetwork\src2\src2'
path = 'G:\complexnetwork\src1\src1'
file = []
for i in os.listdir(path):
    file.append(i.split(".")[0])

nodeid_list = []
ele_id = {}
node_list = []
edges_list = []
coreness_list = []
cc_list = []
nodeid_set = set()
index = 0
jndex = 0
for i in file:
    jsname = path + "\\" + i + '.json'
    with open(jsname, "r", encoding='utf-8') as f:
        jsfile = f.read()
        load_dict = json.loads(jsfile)
        nodeid_list.append(load_dict['user_id'])
        ele_id[load_dict['user_id']] = str(index)
        index += 1
        node_list.append(load_dict['user_name'])
        nodeid_set.add(load_dict['user_id'])
        coreness_list.append(load_dict['coreness'])
        cc_list.append(load_dict['cc'])
        edges = []
        for e in load_dict['follows_list']:
            edges.append(e['userId'])
        for e in load_dict['fans_list']:
            edges.append(e['userId'])
        edges_list.append(edges)

for j in range(len(node_list)):
    node = ef.Element('node')
    attvs = ef.Element('attvalues')
    attv = ef.Element('attvalue')
    attv.set('for', 'modularity_class')
    setval = 0
    if cc_list[j] == 0:
        setval = 0
    elif cc_list[j] < 0.1:
        setval = 1
    elif cc_list[j] < 0.5:
        setval = 2
    elif cc_list[j] < 1:
        setval = 3
    else:
        setval = 4
    attv.set('value', str(setval))
    # attv.set('value', '0')
    attv_id = ef.Element('attvalue')
    attv_id.set('for', 'id_class')
    attv_id.set('value', str(nodeid_list[j]))
    attvs.append(attv)
    attvs.append(attv_id)
    node.set('id', str(ele_id[nodeid_list[j]]))
    node.set('label', str(node_list[j]))
    node.append(attvs)
    nodes.append(node)
    for e in edges_list[j]:
        if e in nodeid_set:
            edge = ef.Element('edge')
            edge.set('id', str(jndex))
            jndex += 1
            edge.set('source', ele_id[nodeid_list[j]])
            edge.set('target', ele_id[e])
            edges_.append(edge)
    print(nodeid_list[j], node_list[j])

if 1 == 0:
    with open('COMPLEX/add_edge.json', "r") as c:
        dm = json.load(c)
        add_i = dm['i']
        add_j = dm['j']
    path = 'G:\complexnetwork\src1\src1'
    file = []
    file_map = {}
    for hjc in range(len(add_j)):
        edge = ef.Element('edge')
        edge.set('id', str(jndex))
        jndex += 1
        edge.set('source', str(add_i[hjc]))
        edge.set('target', str(add_j[hjc]))
        edges_.append(edge)



tree.write('COMPLEX/netc.grxf', encoding='utf-8')
# tree.write('COMPLEX/netx.grxf', encoding='utf-8')


