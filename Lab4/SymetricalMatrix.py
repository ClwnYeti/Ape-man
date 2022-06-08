import numpy as np


class SymmetricalMatrix:
    @staticmethod
    def random_symmetrical_matrix(n: int) -> np.array:
        matrix = np.random.randint(-1000, 1000, size=(n, n))

        for i in range(n):
            for j in range(n):
                if i > j:
                    matrix[i][j] = matrix[j][i]

        return matrix

    @staticmethod
    def symmetrical_matrix_with_diagonal_dominance(k, n):
        matrix = np.random.uniform(-n ** 3, n ** 3, size=(n, n))
        for i in range(n):
            if matrix[i][i] == 0:
                matrix[i][i] = np.random.randint(1, n ** 3)

        for i in range(n):
            for j in range(n):
                if i != j:
                    matrix[i][j] = matrix[i][i] / (k * 1.0) * np.random.randint(-n ** 2, n ** 2 + 1)
            matrix[i][i] *= k ** 2

        for i in range(n):
            for j in range(n):
                if i != j:
                    matrix[i][j] = min(abs(matrix[i][j]), abs(matrix[j][i]))
                    matrix[j][i] = matrix[i][j]

        return matrix
