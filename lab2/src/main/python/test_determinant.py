import unittest
from methods import matrix


class TestDeterminant(unittest.TestCase):
    def test_determinant_1(self):
        self.assertIs(matrix.find_det([1]), False, "Should be False")

    def test_determinant_11(self):
        self.assertEqual(matrix.find_det([[1]]), 1, "Should be 1")

    def test_determinant_12(self):
        self.assertIs(matrix.find_det([[1, 2]]), False, "Should be False")

    def test_determinant_21(self):
        self.assertIs(matrix.find_det([[1], [2]]), False, "Should be False")

    def test_determinant_22(self):
        self.assertEqual(matrix.find_det([[1, 2],
                                          [0, 2]]),
                         2, "Should be 2")

    def test_determinant_22_tuple(self):
        self.assertEqual(matrix.find_det(((1, 2),
                                          (0, 2))),
                         2, "Should be 2")

    def test_determinant_33(self):
        self.assertEqual(matrix.find_det([[1, 2, 3],
                                          [0, 1, 5],
                                          [0, 0, 2]]),
                         2, "Should be 2")

    def test_determinant_44(self):
        self.assertEqual(matrix.find_det([[1, 2, 3, 4],
                                          [0, 1, 2, 3],
                                          [0, 0, 1, 2],
                                          [0, 0, 0, 2]]),
                         2, "Should be 2")


if __name__ == '__main__':
    unittest.main()
