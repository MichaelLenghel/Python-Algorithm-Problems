import unittest
import str_compression as sc

class test_str_compression(unittest.TestCase):
	def test_sentence_reversal(self):
		self.assertEqual(sc.compress(''), None)
		self.assertEqual(sc.compress('AABBCC'), 'A2B2C2')
		self.assertEqual(sc.compress('AAABCCDDDDD'), 'A3B1C2D5')
		print("ALL TEST CASES PASSED")
		
if __name__ == '__main__':
	unittest.main()

