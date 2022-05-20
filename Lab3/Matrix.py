class Matrix:
    def __init__(self, n: int):
        self.n = n
        self._values = [[0 for _ in range(n)] for _ in range(n)]

    def get_values_from_matrix(self, matrix):
        for i in range(self.n):
            for j in range(self.n):
                self._values[i][j] = matrix[i][j]

    def __getitem__(self, i, j):
        return self._values[i][j]

    def __setitem__(self, i, j, value):
        self._values[i][j] = value
