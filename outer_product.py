import numpy as np
import numpy.linalg as la
from numpy.typing import NDArray


def mult(A: NDArray, B: NDArray) -> NDArray:
    # A - row, B - matrix (2,0)
    # C_ilt = np.array([[[10, -2, -6], [-5, 1, 3], [10, -2, -6]], [[10, -10, -10], [-5, 5, 5], [10, -10, -10]], [[-2, -2, -4], [1, 1, 2], [-2, -2, -4]]])
    result = np.zeros((4, 4, 4))
    for k in range(4):
        for i in range(4):
            for j in range(4):
                result[k][i][j] = A[i] * B[j][k]
    print(result)
    return result


def asymmetrisation(C_ilt: NDArray) -> NDArray:
    # C_ilt = np.array([
    #     [[],
    #      [-6, 7, -7],
    #      [5, 4, -1],
    #      []],
    #
    #     [[6, 3, 0],
    #      [4, -4, 6],
    #      [-1, -6, 7],
    #      []],
    #
    #     [[6, 2, 5],
    #      [-6, 1, 5],
    #      [-7, 4, -5],
    #      []],
    #
    #     [[-5, -2, 8],
    #      [-6, 7, -7],
    #      [],
    #      []]
    # ])

    C_lti = np.zeros_like(C_ilt)
    for t in range(4):
        for i in range(4):
            for l in range(4):
                C_lti[t][i][l] = C_ilt[i][l][t]

    C_til = np.zeros_like(C_ilt)
    for t in range(4):
        for i in range(4):
            for l in range(4):
                C_til[t][i][l] = C_ilt[l][t][i]

    C_itl = np.zeros_like(C_ilt)
    for t in range(4):
        for i in range(4):
            for l in range(4):
                C_itl[t][i][l] = C_ilt[l][i][t]

    C_tli = np.zeros_like(C_ilt)
    for t in range(4):
        for i in range(4):
            for l in range(4):
                C_tli[t][i][l] = C_ilt[i][t][l]

    C_lit = np.zeros_like(C_ilt)
    for t in range(4):
        for i in range(4):
            for l in range(4):
                C_lit[t][i][l] = C_ilt[t][l][i]

    return 1/2 * (C_ilt + C_lti + C_til - C_itl - C_tli - C_lit)


def first_task_solver(row_vector: NDArray, matrix: NDArray) -> str:
    def stringify_geolin(A: NDArray):
        result = "["
        for d in range(4):
            for j in range(4):
                for p in range(4):
                    result += str(A[j][d][p])
                    if p != 3:
                        result += ', '
                if j != 3:
                    result += ', '
            if d != 3:
                result += "; "
        result += "]"
        return result
    tmp = mult(row_vector, matrix)
    return stringify_geolin(asymmetrisation(tmp))


print(first_task_solver(np.array([-15, -9, 12, -6]), np.array([[0, -27, 45, 27],
                                                               [27, 0, -45, -45],
                                                               [-45, 45, 0, 30],
                                                               [-27, 45, -30, 0]])))

# [0.0, 0.0, 0.0, 0.0,        0.0, 0.0, -756.0, -1080.0,    0.0, 756.0, 0.0, 1044.0,          0.0, 1080.0, -1044.0, 0.0;
# 0.0, 0.0, 756.0, 1080.0,     0.0, 0.0, 0.0, 0.0,           -756.0, 0.0, 0.0, -540.0,         -1080.0, 0.0, 540.0, 0.0;
# 0.0, -756.0, 0.0, -1044.0,   756.0, 0.0, 0.0, 540.0,       0.0, 0.0, 0.0, 0.0,               1044.0, -540.0, 0.0, 0.0;
# 0.0, -1080.0, 1044.0, 0.0,   1080.0, 0.0, -540.0, 0.0,     -1044.0, 540.0, 0.0, 0.0,         0.0, 0.0, 0.0, 0.0]
