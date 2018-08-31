import unittest
import recursive_reverse_string as reverse_S

class test_reverse_String(unittest.TestCase):
	def test_reverse_String(self):
		self.assertEqual(reverse_S.reverse("hello"), "olleh")
		self.assertEqual(reverse_S.reverse("123456"), "654321")

		print("All tests passed")

if __name__ == '__main__':
	unittest.main()