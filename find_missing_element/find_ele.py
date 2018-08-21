# Pass two arrays. First one has all the elements. 
# Second one has its elements shuffeled and one removed.
# Find which element is missing as efficiently as possible.

from random import sample
# Used hash map to achieve O(N) complexity,
def finder(li_full, li_missing):
	count = {}
	# Assign each value from li_missing as a key to the list
	for num in li_missing:
		# Need to say this, as we don't know if this has been previously set to 1. Can use count = collections.defaultdict(int) to get around this.
		if num not in count:
			count[num] = 1
		else:
			count[num] += 1

	# Now we decrement each time li_missing is incurred, leaving only one value, that is the value that li is missing
	for num in li_full:
		if num not in count:
			return num
		else:
			count[num] -= 1

	# Account for duplicate value being taken out. If value is less than 0, than decremented twice:
	missing_ele = [num for num in count if count[num] < 0]
	missing_ele = missing_ele[0]
	return missing_ele

# Alternative algorithm
# Sorted using timsort.
# O(N log N) in worse case so not as good as the algorithm above
def finder_using_sort(arr1, arr2):

	arr1.sort()
	arr2.sort()

	# Zip matches each corresponding element in a list
	for num1, num2 in zip(arr1, arr2):
		# Can return num1, as if num1 != num2 we know num1 is misisng in second array.
		if num1 != num2:
			return num1
	# Otherwise return last element
	return arr[-1]

# We can also use XOR between the numbers in the array, achieving O(N) for both time and space complexity
def finder_XOR(arr1, arr2):
	result = 0

	# Perform an XOR between the numbers in the array
	# arr1+arr2 concats the arrays
	for num in arr1+arr2:
		result^=num
		print("result: ", result)
	return result


if __name__ == '__main__':
	li_full = [5, 16, 23, 77, 22, 9, 10, 22]
	li_shufled = sample(li_full, len(li_full))
	print(li_full)
	li_shufled.pop(2)
	print(li_shufled)
	missing_ele = finder_XOR(li_full, li_shufled)

	print("Missing element is {}".format(missing_ele))