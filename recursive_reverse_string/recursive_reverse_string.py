# Program to recursively reverse a string

def reverse(s):
	# Base Case
	if s == "":
		return s
	# Recursive calls
	else:
		return reverse(s[1:]) + s[0]
		# return s[-1:] + reverse(s[:len(s) - 1])
		# return s[len(s) - 1] + reverse(s[:len(s) - 1])
		
if __name__ == "__main__":
	print(reverse("Hello, world!"))
# Normal approach: print("Hello, world"[::-1])
