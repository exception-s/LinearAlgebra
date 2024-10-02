import numpy as np
import numpy.linalg as nl
from numpy.typing import NDArray
import scipy.linalg as sp
from sympy import Matrix


np.set_printoptions(precision=6, suppress=True)
L = np.array([[-3, -3, 3],
              [3, 6, -3],
              [-12, -15, 9],
              [21, 24, -18]])
gram_matrix = np.array([[5, -10, -21, -4, 29],  # TODO GRAM IF NEEDED
                        [-10, 22, 45, 8, -63],
                        [-21, 45, 95, 15, -136],
                        [-4, 8, 15, 6, -16],
                        [29, -63, -136, -16, 203]])
y = np.array([-1, -1, 2, -3, 2])
# Find orthogonal projection of y onto L
# x1, x2, x3 = L[:, 0], L[:, 1], L[:, 2]
x1 = np.array([2, 0, 1, 1, 1])
# M = Matrix([x1 @ G @ x1, y @ G @ x1])    # TODO GRAM IF NEEDED
print(y @ gram_matrix @ x1 / x1 @ gram_matrix @ x1)
# print(x1)
