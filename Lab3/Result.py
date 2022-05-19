import pprint
import numpy as np
from LUDecomposition import LUDecomposition
from SolveLU import SolveLU

A = np.random.randint(1, 10, (4, 4))
print("A:")
pprint.pprint(A)

LU = LUDecomposition.decompose_to_LU(A)
print("LU:")
pprint.pprint(LU)

L = LUDecomposition.get_L(LU)
print("L:")
pprint.pprint(L)

U = LUDecomposition.get_U(LU)
print("U:")
pprint.pprint(U)

for i in range(4):
    b = np.zeros((4, 1))
    b[i][0] = 1
    Solution = SolveLU.solve_LU(LU, b)
    pprint.pprint(Solution)
