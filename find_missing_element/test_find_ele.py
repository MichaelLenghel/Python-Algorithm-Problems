import unittest
import find_ele

class test_find_ele(unittest.TestCase):
	def test_array_pair_sum(self):
		self.assertEqual(find_ele.finder([5,5,7,7],[5,7,7]),5)
		self.assertEqual(find_ele.finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
		self.assertEqual(find_ele.finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
		print("All tests passed")


if __name__ == '__main__':
	unittest.main()