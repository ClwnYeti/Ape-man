from Matrix import Matrix


class LUDecomposition:
    @staticmethod
    def decompose_to_LU(a):
        L = Matrix(a.n)
        U = Matrix(a.n).get_values_from_matrix(a)
        for i in range(a.n):
            for j in range(a.n):
                L[j][i] = U[j][i] / U[i][i]

        for k in range(a.n):
            for i in range(a.n):
                for j in range(a.n):
                    L[j][i] = U[j][i] / U[i][i]

            for i in range(k, a.n):
                for j in range(k - 1, a.n):
                    U[i][j] = U[i][j]-L[i][k-1] * U[k-1][j]

        return L, U
