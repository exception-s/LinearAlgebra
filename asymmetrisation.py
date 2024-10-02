import numpy as np
import numpy.linalg as la
from numpy.typing import NDArray


def asymmetrisation() -> NDArray:
    C_ilt = np.array([
        [[],
         [-6, 7, -7],
         [5, 4, -1],
         []],

        [[6, 3, 0],
         [4, -4, 6],
         [-1, -6, 7],
         []],

        [[6, 2, 5],
         [-6, 1, 5],
         [-7, 4, -5],
         []],

        [[-5, -2, 8],
         [-6, 7, -7],
         [],
         []]
    ])

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


print(asymmetrisation())
