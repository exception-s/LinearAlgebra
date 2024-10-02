import numpy as np
import numpy.linalg as nl
from numpy.typing import NDArray
import scipy.linalg as sp
from sympy import Matrix

def custom_scalar(v1, v2):
    return v1.T @ gram_matrix @ v2


gram_matrix = np.array([[7, -10, 24, 52],  # if needed
                        [-10, 22, -48, -101],
                        [24, -48, 107, 226],
                        [52, -101, 226, 479]
                        ])

operator = np.array([[1, 0, 0, -1],
                     [-2, 1, -1, 0],
                     [-3, 1, 0, 2],
                     [-1, 0, -1, 1]])

basis_prev = np.array([[1, -1, 3],
                       [-1, 2, -5],
                       [-1, 2, -4]
                       ])
basis_new = np.array([[1, 1, 0],
                       [-1, 0, 1],
                       [-2, -1, 2]
                       ])
v1 = np.array([3, 1, 2, 0, 0])
v2 = np.array([])
C = np.linalg.inv(basis_prev) @ basis_new
# result = C.T @ gram_matrix @ C
g_inv = np.linalg.inv(gram_matrix)
print((g_inv @ operator.T @ gram_matrix).round(4))