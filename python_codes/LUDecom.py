import numpy as np
from scipy.linalg import lu
A = np.array([[1, 2, 3], [2, 5, 7], [1, 5, 3]])
P, L, U = lu(A)  
print("L:\n", L)
print("U:\n", U)