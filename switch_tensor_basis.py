import numpy as np
import numpy.linalg as la

A = np.array([
     [1, 3, -1, -5],
     [1, -3, -3, -4],
     [-5, -5, -2, 5],
     [-2, 2, 1, 5]
])

old_basis = np.array([[1, -1, -2, -2],
                      [1, 0, -4, -1],
                      [2, -1, -5, -1],
                      [3, 0, -11, 0]])

new_basis = np.array([[-1, 2, -1, -1],
                      [1, -1, -1, 2],
                      [-1, 3, -4, 2],
                      [2, -5, 6, -2]])
T = la.inv(old_basis) @ new_basis
S = la.inv(T)
print(np.einsum("ik, jm, km -> ij", S, S, A))

