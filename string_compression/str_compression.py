# Compress a stirng. Example: 'AAAAABBBBCCCC' becomes A5B4C4
# Complexity: O(N)

import collections

def compress(s):
	count = collections.defaultdict(int)
	compressed_str = ""

	if len(s) == 0:
		print("String must have a length of minimum one")
		return None

	for letter in s:
		count[letter] += 1

	for letter in count:
		compressed_str = compressed_str + letter + str(count[letter])

	return compressed_str

if __name__ == '__main__':
	normal_str = 'AAAAABBBBCCCC'
	print(compress(normal_str))