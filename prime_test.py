import unittest
from prime_numbers import PrimeNumbers


class TestNUmberIsPrime(unittest.TestCase):

	def test_if_greater_than_1(self):
		self.assertFalse(PrimeNumbers.is_prime(5))

	def test_if_equal_to_2(self):
		self.assertEqual(PrimeNumbers.is_equal(2==2))


if __name__ == '__main__':
	unittest.main()

