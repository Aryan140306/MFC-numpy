import numpy as np

# Function to encode a message using matrix multiplication
def encode_message(message, encoding_matrix):
    # Convert message to list of numbers (A=0, B=1,...)
    message = message.upper().replace(" ", "")
    char_to_num = lambda c: ord(c) - ord('A')
    nums = [char_to_num(c) for c in message]
    
    # Pad message to fit matrix size
    n = encoding_matrix.shape[0]
    padding_size = (-len(nums)) % n
    nums.extend([23]*padding_size)  # Fill with 'X' if needed
    
    # Convert to matrix form with columns as blocks
    message_matrix = np.array(nums).reshape(-1, n).T
    
    # Encode by multiplying with encoding matrix
    coded_matrix = np.dot(encoding_matrix, message_matrix) % 26
    return coded_matrix

# Function to decode coded message
def decode_message(coded_matrix, encoding_matrix):
    decoding_matrix = np.linalg.inv(encoding_matrix)
    # Round results and mod 26
    decoded_matrix = np.dot(decoding_matrix, coded_matrix)
    decoded_matrix = np.round(decoded_matrix).astype(int) % 26
    
    # Convert back to text
    num_to_char = lambda i: chr(i + ord('A'))
    decoded_nums = decoded_matrix.T.flatten()
    decoded_chars = ''.join(num_to_char(i) for i in decoded_nums)
    return decoded_chars

# Function to check diagonalizability and verify Cayley-Hamilton theorem
def diagonal_check_and_cayley_hamilton(matrix):
    eigvals, eigvecs = np.linalg.eig(matrix)
    rank = np.linalg.matrix_rank(eigvecs)
    diagonalizable = (rank == matrix.shape[0])
    
    # Cayley-Hamilton verification
    char_poly_coeffs = np.poly(matrix)
    n = matrix.shape[0]
    pA = np.zeros_like(matrix, dtype=float)
    for i, coeff in enumerate(char_poly_coeffs):
        power = n - i
        if power > 0:
            pA += coeff * np.linalg.matrix_power(matrix, power)
        else:
            pA += coeff * np.eye(n)
            
    ch_verified = np.allclose(pA, np.zeros_like(matrix))
    return eigvals, diagonalizable, ch_verified

# User input
message = "Linear Algebra is fun"
print("Original message:", message)

# Example nonsingular (invertible) 3x3 matrix
encoding_matrix = np.array([[2, 5, 1],
                            [1, 3, 1],
                            [1, 2, 1]])

# Encode message
coded = encode_message(message, encoding_matrix)
print("Encoded message matrix:\n", coded)

# Decode message
decoded = decode_message(coded, encoding_matrix)
print("Decoded message:", decoded)

# Check diagonalizability and Cayley-Hamilton
eigvals, is_diag, ch_verified = diagonal_check_and_cayley_hamilton(encoding_matrix)
print("Eigenvalues:", eigvals)
print("Is matrix diagonalizable?", is_diag)
print("Cayley-Hamilton theorem verified?", ch_verified)
