import numpy as np
import numpy.linalg.linalg

a1 = np.array([[-1],
               [0],
               [-2],
               [1],
               [0]])

a2 = np.array([[3],
               [0],
               [2],
               [0],
               [1]])

a3 = np.array([[0],
               [0],
               [0],
               [0],
               [0]])

gram_matrix = np.array([[14, -21, -11, -11, -19],
                        [-21, 34, 15, 13, 31],
                        [-11, 15, 10, 11, 13],
                        [-11, 13, 11, 14, 11],
                        [-19, 31, 13, 11, 29]])
inv_gram = numpy.linalg.inv(gram_matrix)

v1 = inv_gram @ a1
v2 = inv_gram @ a2
v3 = inv_gram @ a3

np.set_printoptions(precision=4, suppress=True)
print(v1)
print(v2)
print(v3)
