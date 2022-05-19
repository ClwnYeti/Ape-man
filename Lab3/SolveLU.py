import numpy as np


class SolveLU:

    def solve_LU(lu_matrix, b):
        """Solve system of equations from given LU-matrix and vector b of absolute terms.
        :param lu_matrix: numpy LU-matrix
        :param b: numpy matrix of absolute terms [n x 1]
        :return: numpy matrix of answers [n x 1]
        """
        # get supporting vector y
        y = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
        for i in range(y.shape[0]):
            y[i, 0] = b[i, 0] - lu_matrix[i, :i] * y[:i]

        # get vector of answers x
        x = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
        for i in range(1, x.shape[0] + 1):
            x[-i, 0] = (y[-i] - lu_matrix[-i, -i:] * x[-i:, 0]) / lu_matrix[-i, -i]

        return x
