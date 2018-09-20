# Problem: Return the range of indexses from a sorted list that start swith a given prefix.

"""
Complexity: O(log N) + X where 'X' is the number of words with prefixses of the type specified.
Binary search will get the mid index in O(log N). We then iterate through the following prefixses in front and behind it in order to find the start and end ranges.
"""

# Finds and returns a word with a given prefix
def binary_search(li, key, left, right):
	len_prefix = len(key)

	while left <= right:
		mid = (left + right) // 2
		print(mid)
		# If prefix is greater than word, than we need to compare using word, rather than list slicing
		if len(li[mid]) < len_prefix:
			if key < li[mid]:
				right = mid - 1
			else:
				left = mid + 1
			continue

		if key == li[mid][:len_prefix]:
			return mid
			# return get_indexses(li, mid, prefix)
		elif key < li[mid][:len_prefix]:
			right = mid - 1
		else:
			left = mid + 1

	return None

# Will return the start and endrange of a given prefix
def get_indexses(words, prefix):

	# Gets a word with a prefix in the list.
	# Since list is sorted we can find the other words iteratively
	mid_index = binary_search(words, prefix, 0, len(words) - 1)

	if mid_index == None:
		return (-1, -1)

	start_index = end_index = mid_index
	len_prefix = len(prefix)
	len_list = len(words) - 1

	# Cannot go backwards if at zero
	if start_index != 0:
		# Iterates until meets word before prefix in list
		while words[start_index - 1][:len_prefix] == prefix:
			if len(words[mid_index]) < len_prefix:
				continue
			start_index -= 1

	if end_index != len_list:
		# Iterates until meets word after prefix in list
		while words[end_index + 1][:len_prefix] == prefix:
			if len(words[mid_index]) < len_prefix:
				continue
			end_index += 1

	return start_index, end_index

# Driver code
if __name__ == "__main__":
	words = ["an", "circumstance", "circus", "devalue", "embrace", "forecast", "prefix",\
				 "predetermine", "pre-intermediate", "pre-teen", "superfood", "thermometer",\
				 "t", "unicycled"]
	prefix = "unicycled"

	start_index, end_index = get_indexses(words, prefix)
	if start_index == -1:
		print("Prefix not found")
	else:
		print("Start index: ", start_index)
		print("End index: ", end_index)

		while start_index <= end_index:
			print(words[start_index], end="")
			start_index += 1
			# Don't print a comma at the end of the last word
			if start_index <= end_index:
				print(end=", ")