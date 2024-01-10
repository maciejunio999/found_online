import numpy as np

def funk(A, b):
    # Check if A is singular
    if np.linalg.det(A) == 0:
        print('Macierz jest osobliwa.')
    else:
        # Perform QR decomposition
        Q, R = np.linalg.qr(A)

        # Check if A equals Q * R
        if not np.allclose(A, Q @ R):
            print('Coś nie tak')

        else:
            # Calculate the inverse of R
            odwR = np.linalg.inv(R)

            # Transpose Q
            Qt = np.transpose(Q)

            # Solve the linear system
            y = Qt @ b
            x = odwR @ y

            print("Solution vector (x):")
            print(x)
            print("\nIntermediate vector (y):")
            print(y)

# Example usage:
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([10, 11, 12])

funk(A, b)

# Another example with a non-singular matrix
A_non_singular = np.array([[2, 1], [1, 3]])
b_non_singular = np.array([4, 5])

funk(A_non_singular, b_non_singular)

A_another = np.array([[1, 2], [4, 5]])
b_another  = np.array([5, 11])

funk(A_another, b_another)
