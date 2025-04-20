import numpy as np
A = np.array([[2, 4, -2, -2], [1, 2, 4, -3], [-3, -3, 8, -2], [-1, 1, 6, -3]])
b = np.array([-4, 5, 7, 7])
x = np.linalg.solve(A, b)
print("Solution using numpy.linalg.solve:", x)
