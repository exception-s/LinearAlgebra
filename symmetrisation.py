import numpy as np
import numpy.linalg as la
from numpy.typing import NDArray


def symmetrisation() -> NDArray:
    C_ilt = np.array([
        [[-4, 0],
         [-5, -2]],

        [[-6, 5],
         [-4, 1]]
    ])

    C_lti = np.zeros_like(C_ilt)
    for t in range(2):
        for i in range(2):
            for l in range(2):
                C_lti[t][i][l] = C_ilt[i][l][t]

    C_til = np.zeros_like(C_ilt)
    for t in range(2):
        for i in range(2):
            for l in range(2):
                C_til[t][i][l] = C_ilt[l][t][i]

    C_itl = np.zeros_like(C_ilt)
    for t in range(2):
        for i in range(2):
            for l in range(2):
                C_itl[t][i][l] = C_ilt[l][i][t]

    C_tli = np.zeros_like(C_ilt)
    for t in range(2):
        for i in range(2):
            for l in range(2):
                C_tli[t][i][l] = C_ilt[i][t][l]

    C_lit = np.zeros_like(C_ilt)
    for t in range(2):
        for i in range(2):
            for l in range(2):
                C_lit[t][i][l] = C_ilt[t][l][i]

    return 1/6 * (C_ilt + C_lti + C_til + C_itl + C_tli + C_lit)


print(symmetrisation())
