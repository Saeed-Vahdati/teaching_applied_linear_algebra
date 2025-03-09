import numpy as np

# Function to calculate the inverse of a matrix
def matrix_inverse(matrix):
    """
    Calculate the inverse of a square matrix.

    Parameters:
    matrix (numpy.ndarray): A square matrix (n x n).

    Returns:
    numpy.ndarray: The inverse of the input matrix.
    """
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The input matrix must be square (n x n).")

    # Calculate the determinant of the matrix
    det = np.linalg.det(matrix)
    if det == 0:
        raise ValueError("The matrix is singular (determinant is 0). Inverse does not exist.")

    # Calculate the inverse using numpy's built-in function
    inverse = np.linalg.inv(matrix)
    return inverse

# Example usage
if __name__ == "__main__":
    # Define a 3x3 matrix
    A = np.array([[1, 2, 3],
                  [0, 1, 4],
                  [5, 6, 0]])

    print("Original Matrix A:")
    print(A)

    try:
        # Calculate the inverse of matrix A
        A_inv = matrix_inverse(A)
        print("\nInverse of Matrix A:")
        print(A_inv)

        # Verify the result by multiplying A with its inverse (should yield the identity matrix)
        identity_matrix = np.dot(A, A_inv)
        print("\nVerification (A * A_inv):")
        print(identity_matrix)
    except ValueError as e:
        print(e)
