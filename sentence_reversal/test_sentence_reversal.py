import unittest
import sentence_reversal as sr

class test_sr(unittest.TestCase):
	def test_sentence_reversal(self):
		self.assertEqual(sr.rev_word('    space before'),'before space')
		self.assertEqual(sr.rev_word('space after     '),'after space')
		self.assertEqual(sr.rev_word('   Hello John    how are you   '),'you are how John Hello')
		self.assertEqual(sr.rev_word('1'),'1')
		print("ALL TEST CASES PASSED")
		
if __name__ == '__main__':
	unittest.main()

