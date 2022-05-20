class SparseMatrix:
    def __init__(self, n: int):
        self._n = n
        self._values = dict()

    def get_values_from_matrix(self, matrix):
        for i in range(self._n):
            for j in range(self._n):
                self._values[(i, j)] = matrix[i][j]

    def __getitem__(self, i, j):
        if (i, j) in self._values.keys():
            return self._values[(i, j)]
        else:
            return 0

    def __setitem__(self, i, j, value):
        self._values[(i, j)] = value
