import numpy as np

def strassen(A, B):
    n = A.shape[0]
    
    # Base case for recursion
    if n == 1:
        return A * B
    
    # Splitting matrices into quadrants
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Computing the 7 products
    P1 = strassen(A11 + A22, B11 + B22)
    P2 = strassen(A21 + A22, B11)
    P3 = strassen(A11, B12 - B22)
    P4 = strassen(A22, B21 - B11)
    P5 = strassen(A11 + A12, B22)
    P6 = strassen(A21 - A11, B11 + B12)
    P7 = strassen(A12 - A22, B21 + B22)

    # Computing the four sub-matrices of C
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combining the four sub-matrices into a single matrix C
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    
    return C

# Example matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication using Strassen's algorithm
result = strassen(A, B)
print("Result of Strassen's Algorithm:")
print(result)

# Compare with numpy's built-in matrix multiplication for verification
numpy_result = np.dot(A, B)
print("\nResult using NumPy's dot product:")
print(numpy_result)
