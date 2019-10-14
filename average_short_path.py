import numpy as np
path = 'shortest_matrix.txt'

with open(path, "r") as f:
    matrix = np.loadtxt(f)
m_shape = np.array(matrix).shape
length = m_shape[0]

asp = 0
for i in range(length):
    for j in range(length):
        asp += matrix[i][j]
asp /= (length*(length - 1))

print(asp)
