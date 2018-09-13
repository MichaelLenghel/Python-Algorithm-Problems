# Palindrome - Uses queue and stack to check if a word is a palindrome e.g. RACECAR would return True

class Queue:
	def __init__(self):
		self.queue_li = []

	def enqueue(self, letter):
		self.queue_li.insert(0, letter)

	def dequeue(self):
		return self.queue_li.pop()

class Stack:
	def __init__(self):
		self. stack_li = []

	def push(self, letter):
		self.stack_li.append(letter)

	def pop(self):
		return self.stack_li.pop()

class check_palindrome:
	def is_paly(self, pal):
		s = Stack()
		q = Queue()

		# Push and enqueue each element onto the stack
		for letter in pal:
			s.push(pal)
			q.enqueue(pal)

		for letter in pal:
			if s.pop() != q.dequeue():
				return pal + " is not a palindrome"

		return pal + " is a palindrome"


chk_paly = check_palindrome()
pal1 = "racecar"
pal2 = "not"

print(chk_paly.is_paly(pal1))
print(chk_paly.is_paly(pal2))








