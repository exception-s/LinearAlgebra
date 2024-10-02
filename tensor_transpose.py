import numpy as np
import numpy.linalg as la

A = np.array([
     [[2, -6],
      [-4, -4]],

     [[4, -4],
      [-6, 5]]
])

print(np.einsum("ijm -> imj", A))
