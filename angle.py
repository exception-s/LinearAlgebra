import numpy as np

gram_matrix = np.array([[76, -106, 50],  # if needed
                        [-106, 148, -70],
                        [50, -70, 34]])

v1 = np.array([-3, -4, -3])
v2 = np.array([1, -4, -5])

sc = v1.T @ gram_matrix @ v2
v1_norm = (v1.T @ gram_matrix @ v1)**0.5
v2_norm = (v2.T @ gram_matrix @ v2)**0.5

print(np.arccos(sc / (v1_norm * v2_norm)))
