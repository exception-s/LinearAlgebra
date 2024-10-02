import numpy as np

A = np.array([
    [5, 2, 0],
    [-4, -6, 1],
    [-2, 2, -2]
])

B = np.array([4, -2, 0])

C = np.array([
    [-1, -3, 0],
    [-1, 5, -4],
    [-6, -2, -3]
])
D = np.einsum("kr, r, kl -> l", A, B, C)
print(D)
