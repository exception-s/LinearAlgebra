import numpy as np
import numpy.linalg as nl
from numpy.typing import NDArray
import scipy.linalg as sp
from sympy import Matrix


def basis_switch(G: NDArray, T: NDArray) -> NDArray:
    return T.transpose() @ G @ T


gram_matrix = np.array([[3, 4, -4, 2, -4],
                        [4, 15, -6, -2, -6],
                        [-4, -6, 7, -2, 8],
                        [2, -2, -2, 4, -2],
                        [-4, -6, 8, -2, 10]])
T = np.array([[-5, -2, 8, 6, 4],
              [0, -1, 0, -2, 2],
              [-2, -2, 3, 0, 2],
              [2, 0, -4, -3, -2],
              [0, 0, 0, 0, 1]])
print(basis_switch(gram_matrix, T))
