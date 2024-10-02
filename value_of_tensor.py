import numpy as np

A = [
    [[[[-5, 4], [-3, -4]], [

        [6, -1], [0, -6]]], [[[1, -3], [4, -1]], [[-2, 5], [-4, -2]]]],

    [[[[3, -4], [-5, 3]], [[3, 1], [-3, -2]]], [[[3, 4], [2, 2]], [[-4, 1], [-4, -1]]]]
]
u1 = np.array([-6, 1])
u2 = np.array([5, 0])
u3 = np.array([4, 5])
u4 = np.array([-4, 3])
u5 = np.array([2, -3])

value = 0
for n in range(2):
    for l in range(2):
        for k in range(2):
            for r in range(2):
                for i in range(2):
                    value += A[n][l][k][i][r] * u1[i] * u2[r] * u3[k] * u4[l] * u5[n]
print(value)
