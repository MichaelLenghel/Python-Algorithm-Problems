# Given the first node in a linked list, check if the list contains a cycle.
# My appraoch will be using the set data structure in python


class Node:
	# Proper linked list implemented at end for reference (Insert + delete implemented)
	def __init__(self,value):
		self.value = value
		self.next = None

def cycle_check(node):
	nodes_set = set()

	while node != None:
		if node.next not in nodes_set:
			nodes_set.add(node.next)
			node = node.next
		else:
			return True
	return False



if __name__ == '__main__':
	# CREATE CYCLE LIST
	a = Node(1)
	b = Node(2)
	c = Node(3)

	a.next = b
	b.next = c
	c.next = a # Cycle Here!
	if cycle_check(a):
		print("Cycle found!")
	else:
		print("Cycle not found!")

# class LinkedList:
# 	def __init__(self):
# 		self.head = None
# 		self.tail = None

# 	def insert(self, item):
# 		if self.head is None:
# 			self.head = Node(item)
# 			self.tail = Node(item)
# 		else:
# 			new_node = Node(item)
# 			previous_node = None
# 			current_node = self.head

# 			while current_node != None:
# 				if new_node.item > current_node.item:
# 					previous_node = current_node
# 					current_node = current_node.next
# 				else:
# 					break

# 			# Inserting at head of lists
# 			if previous_node == None:
# 				new_node.next = self.head
# 				self.head = new_node

# 			# Inserting at the end of the list
# 			elif current_node is None:
# 				if self.head.next == None:
# 					self.head.next = new_node
# 				self.tail.next = new_node
# 				self.tail = new_node

# 			# insert at middle
# 			else:
# 				# Need to set link of head to chain to rest of elements
# 				if self.head.next is None:
# 					self.head.next = new_node
# 				previous_node.next = new_node
# 				new_node.next = current_node



# 	def delete(self, item):

# 		if self.is_empty():
# 			print("Must have at least one element in the linkedlist to delete")
# 			return
# 		else:
# 			# Removing from the end of a linked list:
# 			previous_node = None
# 			current_node = self.head

# 			while current_node:
# 				if current_node.item == item:
# 					break
# 				previous_node = current_node
# 				current_node = current_node.next
# 			# Else executes if loop terminates normally and no value found
# 			else:
# 				print("\n", item, " not found in the list", sep="")
# 				return

# 			# Means we are deleting the first element
# 			if previous_node == None:
# 				# Removing from start of a linked list
# 				ele = self.head.item
# 				self.head = self.head.next
# 			else:
# 				ele = current_node.item
# 				previous_node.next = current_node.next
# 			return ele


# 	def is_empty(self):
# 		return self.head == None

# 	def show(self):
# 		temp_head = self.head
# 		print()
# 		while temp_head != None:
# 			print(temp_head.item)
# 			temp_head = temp_head.next
