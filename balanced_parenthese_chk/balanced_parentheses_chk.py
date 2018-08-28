# Problem: In a string with no spaces or extra characters: Check if there is an even number of closing and opening parenthesis in the corrct order.
# Made own stack, rather than using lists directly, although could have used nodes

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.size() == 0:
			print("Must be at least one element in the list")
			return
		else:
			return self.items.pop()

	def peek(self):
		if not self.is_empty():
			return self.items[len(self.items) - 1]
		else:
			return "Size must be greater than 0"

	def is_empty(self):
		return self.items == []

	def size(self):
		return len(self.items)

def balance_chk(s):
	stack = Stack()
	# Handy way of separating a string into separate elements
	open_brackets = ("({[")
	# Initially used a function, to find the reverse of a bracket, but this is cleaner
	bracket_matches = ([ ('{', '}'), ('[', ']'), ('(', ')')])

	# Check edge case. Stack must be even
	if len(s) % 2 != 0:
		return False

	for bracket in s:
		if bracket in open_brackets:
			stack.push(bracket)
		# If most recent bracket and closing bracket make a set, pop
		elif (stack.peek(), bracket) in bracket_matches:
			stack.pop()
		# Incorrect closing bracket
		else:
			return False

	# Stack must be empty for it work, as if not, some opening parenthesis are still there
	if stack.is_empty():
		return True
	else:
		return False


if __name__ == '__main__':
	print(balance_chk('[]'))
	# balance_chk('([)]')