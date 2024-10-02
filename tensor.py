import numpy as np
import numpy.linalg as la


tensor = np.array([
    [[-2, -4, -3],
     [-2, -7, 6],
     [-1, 7, -1]],

    [[5, 4, 8],
     [6, 2, -4],
     [-3, -6, -4]],

    [[6, -4, 4],
     [-5, -4, 0],
     [5, -6, -3]]
])
new_tensor = np.zeros((3, 3, 3))

old_basis = np.array([[1, -1, -2],
                      [-2, 3, 2],
                      [1, -2, 1]])

new_basis = np.array([[-1, -1, 2],
                      [-2, -3, 3],
                      [1, 2, 0]])
T = la.inv(old_basis) @ new_basis
S = la.inv(T)
for x in range(3):
    for y in range(3):
        for z in range(3):
            total = 0
            for i in range(3):
                for j in range(3):
                    for m in range(3):
                        total += T[j][y] * T[m][z] * S[x][i] * tensor[m][i][j]
            new_tensor[z][x][y] = total
print(new_tensor)