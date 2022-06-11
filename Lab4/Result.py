import pprint

import numpy as np

from Lab3.HilbertSolution import HilbertSolution
from JacobiByRotation import JacobiByRotation
from SymetricalMatrix import SymmetricalMatrix

# A = HilbertSolution.hilbert(3)
#
# pprint.pprint(A)
# pprint.pprint(JacobiByRotation.solve(A))

B = HilbertSolution.hilbert(500)
pprint.pprint(B)
JacobiByRotation.solve(B)
pprint.pprint(f"Число обусловленности - {np.linalg.cond(B)}")