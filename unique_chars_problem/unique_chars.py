import collections

def uni_chars(s):
	count = collections.defaultdict(int)

	if len(s) == 0:
		return True

	for letter in s:
		count[letter] += 1
		if count[letter] > 1:
			return False

	return True

# Alternative method - Best but too short for interview:
def uni_chars_2(s):
	# Set makes everything unique. So check len if all unique against len of string. If same -> Unique characters are used
	return len(set(s)) == len(s)

# Alternative method, using our own set
def uni_chars_3(s):
	chars = set()

	for letter in chars:
		if let in chars:
			return False
		else:
			char.add(let)

if __name__ == '__main__':
	normal_str = 'abcdefgf'
	if uni_chars(normal_str):
		print("Strings have all unique values")
	else:
		print("Strings have different values")