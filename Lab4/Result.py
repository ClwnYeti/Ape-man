from Jacobi import jacobi


def hilbert(k):
    return [[1 / (i + j + 1) for j in range(k)] for i in range(k)]


A = hilbert(3)

print(A)
print(jacobi(A))
