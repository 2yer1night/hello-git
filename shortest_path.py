import numpy as np
path = 'matrix(7).txt'

with open(path, "r") as f:
    matrix = np.loadtxt(f)
m_shape = np.array(matrix).shape
length = m_shape[0]
for i in range(length):
    for j in range(length):
        if i != j and matrix[i][j] == 0:
            matrix[i][j] = 10086
print('set ok')
'''
Floyd algorithm O(n^3)
'''
for m in range(length):
    print('done:' + str(m * 100 // length) + '%')
    for i in range(length):
        for j in range(length):
            if matrix[i][j] > matrix[i][m] + matrix[m][j]:
                matrix[i][j] = matrix[i][m] + matrix[m][j]

np.savetxt('shortest_matrix.txt', matrix, fmt="%d", delimiter=' ')