import unittest
from anagram_check import anagram_check

class TestAnagram(unittest.TestCase):
	def test_anagram_check(self):
		# ac.self.anagram_check_sorted
		self.assertEqual(anagram_check('mat', 'tam'), True)
		self.assertEqual(anagram_check('go go go', 'gggooo'), True)
		self.assertEqual(anagram_check('123', '1 2'), False)
		self.assertEqual(anagram_check('abcde', 'aabbcceedd'), False)
		print("All test cases passed!")

# This allows us to compile it normally
if __name__ == '__main__':
	unittest.main()