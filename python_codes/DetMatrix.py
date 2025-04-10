import numpy as np
# Define a 5x5 matrix
A = np.array([
    [2, 1, 3, 4, 5],
    [1, 0, 2, 1, 3],
    [3, 2, 1, 0, 4],
    [4, 1, 0, 2, 1],
    [5, 3, 4, 1, 2]
])
# Compute the determinant
det_A = np.linalg.det(A)
# Display the determinant (rounded to 4 decimal places)
print("\nDeterminant of matrix A:")
print(round(det_A, 4))
