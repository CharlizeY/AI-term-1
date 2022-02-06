import unittest

from euclidean import euclidean_distance

class EuclideanTest(unittest.TestCase):
    def test_positive_input(self):
        dist = euclidean_distance(3, 2, 5, 6)
        expected_answer = 2.828427
        epsilon = 0.000001
        assert abs(dist - expected_answer) < epsilon

    def test_negative_input(self):
        dist = euclidean_distance(-3, -2, 5, 6)
        expected_answer = 10
        epsilon = 0.000001
        assert abs(dist - expected_answer) < epsilon

    def test_zero_input(self):
        dist = euclidean_distance(0, 0, 0, 0)
        expected_answer = 0
        epsilon = 0.000001
        assert abs(dist - expected_answer) < epsilon

if __name__ == '__main__':
    unittest.main()
