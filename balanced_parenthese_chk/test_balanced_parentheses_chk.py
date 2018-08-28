import unittest
import balanced_parentheses_chk as bpc

class test_find_ele(unittest.TestCase):
	def test_array_pair_sum(self):
		self.assertEqual(bpc.balance_chk('[](){([[[]]])}('),False)
		self.assertEqual(bpc.balance_chk('[{{{(())}}}]((()))'),True)
		self.assertEqual(bpc.balance_chk('[[[]])]'),False)
		self.assertEqual(bpc.balance_chk(''),True)
		print("All tests passed")


if __name__ == '__main__':
	unittest.main()