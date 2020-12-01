import unittest
import matrix
import inverse_matrix


class TestDeterminant(unittest.TestCase):
    def test_square_1(self):
        self.assertIs(matrix.is_square_matrix([1]), False, "Should be False")

    def test_square_11(self):
        self.assertIs(matrix.is_square_matrix([[1]]), True, "Should be True")

    def test_square_12(self):
        self.assertIs(matrix.is_square_matrix([1, 2]), False, "Should be False")

    def test_square_21(self):
        self.assertIs(matrix.is_square_matrix([[1], [2]]), False, "Should be False")

    def test_square_22(self):
        self.assertIs(matrix.is_square_matrix([[1, 2], [3, 4]]), True, "Should be True")

    def test_square_22_tuple(self):
        self.assertIs(matrix.is_square_matrix(((1, 2), (3, 4))), True, "Should be True")


if __name__ == '__main__':
    unittest.main()
