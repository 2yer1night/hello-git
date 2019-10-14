import os
import numpy as np
import json
import networkx as nx
import matplotlib.pyplot as plt

path = 'src'
file = []
user_set = {}
limit_set = set()
index = 0
for i in os.listdir(path):
    file.append(i.split(".")[0])
    user_set[i.split(".")[0]] = index
    limit_set.add(i.split(".")[0])
    index += 1
len = len(file)
print(len)
matrix = np.zeros([len, len], int)

n = 0
edge = 0
song = np.zeros([len,100],int)

for i in file:
    jsname = path + "\\" + i + '.json'
    with open(jsname, "r", errors='ignore', encoding='utf-8') as f:
        jsfile = f.read()
        load_dict = json.loads(jsfile)
        for follower in load_dict['follows_list']:
            if str(follower['userId']) in limit_set:
                matrix[int(user_set[str(i)])][int(user_set[str(follower['userId'])])] += 1
        for fan in load_dict['fans_list']:
            if str(fan['userId']) in limit_set:
                matrix[int(user_set[str(i)])][int(user_set[str(fan['userId'])])] += 2
    print(str(n/722*100) + "%")
    n += 1
    continue
for i in range(len):
    for j in range(len):
        if matrix[i][j] == 3:
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0

# np.savetxt('matrix(7).txt', matrix, fmt="%d", delimiter=' ')

