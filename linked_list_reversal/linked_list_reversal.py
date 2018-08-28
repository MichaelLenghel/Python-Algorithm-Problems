# Problem: Function to reverse linked list in place. Function will take head of a list and return a new head of the list

class Node:
	def __init__(self, item):
		self.item = item
		self.next = None

def reverse(head):
	current = head
	previous = None
	next_node = None
	
	while current:
		# Save link to next node
		next_node = current.next
		# set current node to point to the previous one (Initially to None)
		current.next = previous
		# Move previous up one node to what current is
		previous = current
		# Move current to the next node in the list
		current = next_node

	return previous


if __name__ == '__main__':
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)

	a.next = b
	b.next = c
	c.next = d

	print(a.next.item)
	print(b.next.item)
	print(c.next.item)

	reverse(a)
	print("Reversed list: ")
	print(d.next.item)
	print(c.next.item)
	print(b.next.item)