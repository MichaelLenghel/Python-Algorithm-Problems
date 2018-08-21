import unittest
import largest_sum as ls

class test_sum(unittest.TestCase):
	def test_largest_sum(self):
		self.assertEqual(ls.large_cont_sum([1,2,-1,3,4,-1]), 9)
		self.assertEqual(ls.large_cont_sum([1,2,-1,3,4,10,10,-10,-1]), 29)
		self.assertEqual(ls.large_cont_sum([-1,1]), 1)
		self.assertEqual(ls.large_cont_sum([-1,-1, -1]), -1)


if __name__ == '__main__':
	unittest.main()