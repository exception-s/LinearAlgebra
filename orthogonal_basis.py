import numpy as np
from math import *


def custom_scalar(v1, v2):
    return v1.T @ gram_matrix @ v2


def gram_schmidt(V):  # add custom_scalar product if needed
    U = []
    for one in V:
        u = one - sum((custom_scalar(one, ui) / custom_scalar(ui, ui) * ui) for ui in U)
        if np.linalg.norm(u) > 1e-10:
            U.append(u)
    return U


def normalize(v_array):  # add custom_scalar product if needed
    result = []
    for elem in gram_schmidt(v_array):
        result.append(elem / sqrt(custom_scalar(elem, elem)))
    return result


gram_matrix = np.array([[25, 16, 32, -40, 2],  # if needed
                        [16, 23, 26, -8, 2],
                        [32, 26, 44, -44, 2],
                        [-40, -8, -44, 89, -2],
                        [2, 2, 2, -2, 2]
                        ])

vectors = np.array([[2, -2, 4, -8, -14],
                    [0, 2, -2, 4, 10],
                    [-4, 0, -2, 6, 6],
                    [-6, 2, -6, 16, 22]
                    ])
# orthogonal_basis = gram_schmidt(vectors)  # normalize if needed
orthogonal_basis = normalize(gram_schmidt(vectors))

print("Ортогональный базис подпространства L:")
for v in orthogonal_basis:
    print(v.round(4))
