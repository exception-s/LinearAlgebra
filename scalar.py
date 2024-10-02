import numpy as np

gram_matrix = np.array([[7, 4, -6],  # if needed
                        [4, 3, -4],
                        [-6, -4, 6]
                        ])
G = np.array([[15, 14, -26, 0, -36],
              [14, 15, -24, 4, -36],
              [-26, -24, 47, -2, 66],
              [0, 4, -2, 12, -10],
              [-36, -36, 66, -10, 98]])

v1 = np.array([1, -4, -5, 1, 0])
v2 = np.array([0, -5, -5, 3, -3])
y = np.array([1, -1, 1, 2, 1])
x1 = np.array([-3, 9, -27, 9, -24])
x2 = np.array([3, -6, 21, -9, 15])
sc = v1.T @ G @ v2
# sc = x1 @ x1
sc2 = y @ x1
# res = y - (-13/34 * v1 - 13/17 * v2 - 16/17 * v3 + 3/17 * v4)
print(sc)
y_norm = (y.T @ y)**0.5
pr = np.array([57/11, 36/11, -135/11])
pr_norm = (pr.T @ pr)**0.5
# print(np.arccos(pr_norm / y_norm))
