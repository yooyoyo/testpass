# unittest - ibrary to make testing easier
import unittest
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False
    return True


class Tests(unittest.TestCase):

    def test_1(self):
        "Check that 1 is not a prime"
        self.assertFalse(is_prime(1))

    def test_2(self):
        "Check that 2 is prime"
        self.assertTrue(is_prime(2))

    def test_8(self):
        "Check that 8 is not a prime"
        self.assertFalse(is_prime(8))

    def test_11(self):
        "Check that 11 is prime"
        self.assertTrue(is_prime(11))

    def test_25(self):
        "Check that 25 is not a prime"
        self.assertFalse(is_prime(25))


if __name__ == "__main__":
    unittest.main()