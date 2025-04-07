import numpy as np
A = np.array([[2, 3], [4, -1]])
b = np.array([5, 1])
try:
    A_inv = np.linalg.inv(A)  
    x = np.dot(A_inv, b)      
    print("Solution using inverse method:", x)
except np.linalg.LinAlgError:
    print("Matrix is singular!")