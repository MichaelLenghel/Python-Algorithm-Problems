import unittest
import cycle_chk as c_c

# CREATE CYCLE LIST
a = c_c.Node(1)
b = c_c.Node(2)
c = c_c.Node(3)

a.next = b
b.next = c
c.next = a # Cycle Here!


# CREATE NON CYCLE LIST
x = c_c.Node(1)
y = c_c.Node(2)
z = c_c.Node(3)

x.next = y
y.next = z

class test_sum(unittest.TestCase):
	def test_largest_sum(self):
		self.assertEqual(c_c.cycle_check(a), True)
		self.assertEqual(c_c.cycle_check(x), False)
		print("ALL TEST CASES PASSED")

if __name__ == '__main__':
	unittest.main()