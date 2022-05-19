import numpy as np

class LUDecomposition:
    def decompose_to_LU(a):
        """Decompose matrix of coefficients to L and U matrices.
         L and U triangular matrices will be represented in a single nxn matrix.
        :param a: numpy matrix of coefficients
        :return: numpy LU matrix
        """
        # create emtpy LU-matrix
        lu_matrix = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
        n = a.shape[0]

        for k in range(n):
            # calculate all residual k-row elements
            for j in range(k, n):
                lu_matrix[k, j] = a[k, j] - lu_matrix[k, :k] * lu_matrix[:k, j]
            # calculate all residual k-column elemetns
            for i in range(k + 1, n):
                lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]

        return lu_matrix

    def get_L(m):
        """Get triangular L matrix from a single LU-matrix
        :param m: numpy LU-matrix
        :return: numpy triangular L matrix
        """
        L = m.copy()
        for i in range(L.shape[0]):
            L[i, i] = 1
            L[i, i + 1:] = 0
        return np.matrix(L)

    def get_U(m):
        """Get triangular U matrix from a single LU-matrix
        :param m: numpy LU-matrix
        :return: numpy triangular U matrix
        """
        U = m.copy()
        for i in range(1, U.shape[0]):
            U[i, :i] = 0
        return U
