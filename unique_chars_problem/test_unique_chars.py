import unittest
import unique_chars as uc

class test_str_compression(unittest.TestCase):
	def test_sentence_reversal(self):
		self.assertEqual(uc.uni_chars(''), True)
		self.assertEqual(uc.uni_chars('goo'), False)
		self.assertEqual(uc.uni_chars('abcdefg'), True)
		print("ALL TEST CASES PASSED")
		
if __name__ == '__main__':
	unittest.main()

