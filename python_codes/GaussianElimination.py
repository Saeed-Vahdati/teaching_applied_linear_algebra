import numpy as np
A = np.array([[2, 3], [4, -1]])
b = np.array([5, 1])
x = np.linalg.solve(A, b)
print("Solution using numpy.linalg.solve:", x)
