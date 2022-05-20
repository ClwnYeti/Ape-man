import pprint
import time

import numpy as np
from scipy.sparse import csr_matrix

from LUDecomposition import LUDecomposition
from Lab3.HilbertSolution import HilbertSolution
from Lab3.Matrix import Matrix
from Lab3.SparseMatrix import SparseMatrix
from SolveLU import SolveLU

A3 = SparseMatrix(3,3).get_values_from_matrix(np.random.randint(10, size=(3, 3)))
print("A 3x3:")
print(A3)

L, U = LUDecomposition.decompose_to_LU(A3)

print("L:")
print(L)

print("U:")
print(U)

A4 = SparseMatrix(4,4).get_values_from_matrix(np.random.randint(10, size=(4, 4)))
print("A 4x4:")
print(A4)

L, U = LUDecomposition.decompose_to_LU(A4)

print("L:")
print(L)

print("U:")
print(U)

# 1
startTime = time.time()  # время начала замера

HilbertSolution.solve_LU(10)

endTime = time.time()  # время конца замера
totalTime = endTime - startTime  # вычисляем затраченное время
print(totalTime)
#
# # 2
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(50)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 3
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 2)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 5
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 3)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 6
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 4)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 7
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 5)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
#
# # 8
# startTime = time.time()  # время начала замера
#
# HilbertSolution.solve_LU(10 ** 6)
#
# endTime = time.time()  # время конца замера
# totalTime = endTime - startTime  # вычисляем затраченное время
# print(totalTime)
