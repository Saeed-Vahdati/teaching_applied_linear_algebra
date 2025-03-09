import numpy as np

# Define a complex matrix
A = np.array([[1 + 1j, 2],
              [3, 4 - 1j]])

# Calculate the inverse
A_inv = np.linalg.inv(A)

print("Original Matrix A:")
print(A)

print("\nInverse of Matrix A:")
print(A_inv)
