import numpy as np
import numpy.linalg as nl
from numpy.typing import NDArray
import scipy.linalg as sp
from sympy import Matrix

Q = np.array([[8, -21, 12, -29],
              [-21, 56, -32, 79],
              [12, -32, 18, -45],
              [-29, 79, -45, 115]])

T = np.array([[9, 23, -69, 181],
              [-1, 0, 3, -9],
              [4, 6, -23, 62],
              [3, 7, -22, 58]])
switch = T.transpose() @ Q @ T
print(switch)
