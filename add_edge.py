import numpy as np
path = 'common_friends.txt'

with open(path, "r") as f:
    matrix = np.loadtxt(f)
path = 'common_songs.txt'

with open(path, "r") as f:
    matrix2 = np.loadtxt(f)
m_shape = np.array(matrix).shape
length = m_shape[0]

for i in range(length):
    for j in range(length):
        matrix2[i][j] += 2*matrix[i][j]


# print(mx)