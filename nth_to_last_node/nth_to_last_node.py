# Given a linked list, get the nth item from the end of a linked list
class Node:

    def __init__(self, value):
        self.item = value
        self.next  = None

# Solution 1: Use a list and pythons string slicing
def nth_to_last_node_list(n, head):
	li = list()
	while head:
		li.append(head)
		head = head.next
	return li[-n]

# Solution 2: Reverse the entire list, than iterate n times through and return the correct element
def nth_to_last_node_reverse(n, head):
	current = head
	previous = None
	next_node = None

	if n <= 0:
		raise LookupError('Error: n must be at least 1')

	# Reverse list
	while current:
		next_node = current.next
		current.next = previous
		previous = current
		current = next_node

	for x in range(n - 1):
		if previous == None:
			raise LookupError('Error: n is larger than the linked list') 
		previous = previous.next

	return previous

# Solution 3: Set the right pointer n times down the list. Then iterate both left and right and when right
# reaches the end, the left will be N times before the list
def nth_to_last_node(n, head):
	left_pointer = head
	right_pointer = head

	for i in range(n-1):
		if not right_pointer.next:
			raise LookupError('Error: n is larger than the linked list')
		right_pointer = right_pointer.next

	while right_pointer.next:
		left_pointer = left_pointer.next
		right_pointer = right_pointer.next

	return left_pointer

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)
print(target_node.item)