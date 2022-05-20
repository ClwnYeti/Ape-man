import numpy as np

from Lab3.LUDecomposition import LUDecomposition
from Lab3.Matrix import Matrix
from Lab3.SolveLU import SolveLU
from Lab3.SparseMatrix import SparseMatrix


class HilbertSolution:
    @staticmethod
    def solve_LU(n):
        A = SparseMatrix(n, n).get_values_from_matrix(np.matrix(HilbertSolution.hilbert(n)))
        L, U = LUDecomposition.decompose_to_LU(A)
        b = Matrix(n,1).get_values_from_matrix(np.random.randint(10, size=(n, 1)))
        SolveLU.solve_LU(L, U, b)

    @staticmethod
    def hilbert(n):
        return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
