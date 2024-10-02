import numpy as np

# TODO: find orthogonal basis of subspace and find projection as sum(scalar(v, ui)/scalar(ui, ui) * ui)
#  cos(theta) = norm(projection) / norm(vector)
#  print(theta)

gram_matrix = np.array([[6, 3, -11, -11],  # if needed
                        [3, 2, -5, -5],
                        [-11, -5, 22, 23],
                        [-11, -5, 23, 25]])

vector = np.array([-6, 15, -3, 15])

subspace = np.array([[3, -6, 3, -9],
                    [0, 3, 0, 0],
                    [-3, 6, 0, 9]
                     ])
orthogonal_basis = np.array([[3, -6, 3, 9],
                             [0.4, 2.2, 0.4, -1.2],
                             [-0.2727, 0, 2.7273, 0.8182]
                             ])

projection = sum(np.dot(vector, ui) / np.dot(ui, ui) for ui in orthogonal_basis)
p_norm = np.linalg.norm(projection)
v_norm = np.linalg.norm(vector)

print(np.arccos(p_norm / v_norm))
