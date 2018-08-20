import unittest
import array_pair_sum

class test_pairs(unittest.TestCase):
	def test_array_pair_sum(self):
		self.assertEqual(array_pair_sum.pair_sum([1, 3, 2, 2, 0, 4], 4), 3)
		self.assertEqual(array_pair_sum.pair_sum([1,2,3,1],3),1)
		print("All tests passed")


if __name__ == '__main__':
	unittest.main()