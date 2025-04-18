import numpy as np

def create_zigzag_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    num = 1
    for col in range(n):
        if col % 2 == 0:
            for row in range(n):
                matrix[row][col] = num
                num += 1
        else:
            for row in reversed(range(n)):
                matrix[row][col] = num
                num += 1
    return matrix

def rotate_90_clockwise(matrix):
    # Step 1: Transpose the matrix
    transposed = np.transpose(matrix)
    # Step 2: Reverse each row
    rotated = np.array([row[::-1] for row in transposed])
    return rotated

# Set size
n = 4

# Create zigzag matrix
zigzag_matrix = create_zigzag_matrix(n)

print("Original Zigzag Matrix:")
print(zigzag_matrix)

# Rotate
rotated_matrix = rotate_90_clockwise(zigzag_matrix)

print("\nRotated 90 Degrees Clockwise:")
print(rotated_matrix)
