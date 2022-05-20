class Matrix:
    def __init__(self, *dimension):
        self.n = dimension[0]
        self.m = dimension[1]
        self._values = [[0 for _ in range(self.m)] for _ in range(self.n)]

    def get_values_from_matrix(self, matrix):
        for i in range(self.n):
            for j in range(self.m):
                self._values[i][j] = matrix[i][j]

        return self

    def __getitem__(self, indexes):
        try:
            int(indexes)
            return [self.__getitem__((indexes, j)) for j in range(self.n)]
        except:
            return self._values[indexes[0]][indexes[1]]

    def __setitem__(self, indexes, value):
        self._values[indexes[0]][indexes[1]] = value

    def __str__(self):
        return "[" + "\n".join(["[" + ", ".join([str(round(j, 3)) for j in self.__getitem__(i)]) + "]" for i in range(self.n)]) + "]"

    def __mul__(self, other):
        try:
            other.n
            if self.m != other.n:
                return None
            c = Matrix(self.n, other.m)
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        c[i, j] += self[i, k] * other[k, j]

            return c
        except:
            return Matrix(self.n, self.m).get_values_from_matrix(
                [[self[j, i] * other for i in range(self.m)] for j in range(self.n)])