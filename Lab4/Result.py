import pprint
from Lab3.HilbertSolution import HilbertSolution
from JacobiByRotation import JacobiByRotation

A = HilbertSolution.hilbert(3)

pprint.pprint(A)
pprint.pprint(JacobiByRotation.solve(A))
