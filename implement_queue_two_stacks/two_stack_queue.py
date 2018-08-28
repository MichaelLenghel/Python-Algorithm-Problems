class Queue2Stacks:
	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self, item):
		self.instack.append(item)

	def dequeue(self):
		# Now return in queue order from stack 2
		# If outstack is empty, pop all elements from instack and add them
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())
		return self.outstack.pop()

	def is_empty(self, stack):
		return stack == []

	def peek(self, stack):
		return stack[len(stack) - 1]

if __name__ == '__main__':

	q = Queue2Stacks()

	for i in range(5):
		q.enqueue(i)

	print(q.instack)

	for i in range(4):
		print(q.dequeue(), end=", ")

	q.enqueue(10)
	print(q.dequeue())
	print(q.dequeue())