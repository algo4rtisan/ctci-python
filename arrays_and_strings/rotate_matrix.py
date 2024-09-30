import unittest


# Rotate Matrix: 
# Given an image represented by an NxN matrix, 
# where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. 
# Can you do this in place?
# Example:
# [[1, 2, 3],         [[7, 4, 1], 
#  [4, 5, 6],    ->    [8, 5, 2], 
#  [7, 8, 9]]          [9, 6, 3]]

def rotate_matrix(matrix):
    n = len(matrix)
    for l in range(n // 2):
        for i in range(l, n-l-1):
            temp = matrix[l][i]
            matrix[l][i]=matrix[-i-1][l]
            matrix[-i-1][l]=matrix[-l-1][-i-1]
            matrix[-l-1][-i-1]=matrix[i][-l-1]
            matrix[i][-l-1] = temp
    return matrix


class TestRotateMatrix(unittest.TestCase):
    def test_rotate_matrix(self):
        M_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        M_out = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertEqual(rotate_matrix(M_in), M_out)

if __name__ == "__main__":
    unittest.main()