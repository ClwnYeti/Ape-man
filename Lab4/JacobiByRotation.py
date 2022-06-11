import numpy as np
from numpy import ndarray
from math import *


class JacobiByRotation:
    @staticmethod
    def solve(a, accuracy=0.01):
        n = len(a)
        iterations = 0
        matrix_copy = a.copy()
        vectors = np.eye(n)  # Initialize transformation matrix

        while 1:  # Jacobi rotation loop
            max_element, max_i, max_j = JacobiByRotation._maxElem(matrix_copy)

            if (iterations == 1280):
                x = max_element

            if max_element < accuracy:
                print(iterations)
                print(x / max_element)
                vectors = ndarray.tolist(vectors.T)
                eigenvalues = ndarray.tolist(matrix_copy.diagonal())
                return eigenvalues, vectors

            iterations += 1
            transformation_matrix = JacobiByRotation._rotate(matrix_copy, max_i, max_j, n)
            vectors = vectors.dot(transformation_matrix)

            matrix_copy = transformation_matrix.T.dot(matrix_copy).dot(transformation_matrix)

    @staticmethod
    def _maxElem(a: ndarray):
        n = len(a)
        aMax = 0
        max_i = max_j = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(a[i][j]) > aMax:
                    aMax = abs(a[i][j])
                    max_i = i
                    max_j = j
        return aMax, max_i, max_j

    @staticmethod
    def _rotate(matrix, i, j, n):
        rotation_matrix = np.eye(n)
        phi = 1 / 2 * atan((2 * matrix[i][j]) / (matrix[i][i] - matrix[j][j]))

        rotation_matrix[i][j] = -sin(phi)
        rotation_matrix[j][i] = sin(phi)
        rotation_matrix[i][i] = cos(phi)
        rotation_matrix[j][j] = cos(phi)

        return rotation_matrix
