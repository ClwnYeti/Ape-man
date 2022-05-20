import numpy as np


class SolveLU:
    @staticmethod
    def solve_LU(L, U, b):
        n = L.n
        # (5) Perform substitution Ly=b
        y = [0.0 in range(n)]
        for i in range(0, n, 1):
            y[i] = b[i] / float(L[i, i])
            for k in range(0, i, 1):
                y[i] -= y[k] * L[i, k]

        n = U.n

        # (6) Perform substitution Ux=y
        x = [0 in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = y[i] / float(U[i, i])
            for k in range(i - 1, -1, -1):
                U[i] -= x[i] * U[i, k]

        return x
