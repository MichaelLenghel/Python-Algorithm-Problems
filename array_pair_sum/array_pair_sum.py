""" 
  A less pythonic approach would be to sort all the elements and start with two indexses at opposite sides/
  If combined value is too little, increment from left, if combined value is too large, increment from the right.
  Complexity of this is O(n log n) if we sort with an efficient algorithm such as merge sort.
  If space is not an issue and data set is small, with radix sort could achieve O(NK) complexity. Where N is the numbers in the list and
  is the size of the largest digit in the array

  The algorithm below uses hash sets and achieves O(N) complexity.
  By using two sets we can iterate over the numbers just once.
  This is achieved by adding a number to the set if it is not already there,
  and then on the next run through, check the current target of the number we are 
  dealing with against the previous numers that have been added.

  We use sets to not replicate numbers, as well as to take advantage of the speed that comes from the hashing that sets perform.
"""
def pair_sum(arr, k):
	if len(arr) < 2:
		print("Error array must contain a minimum of two elements")
		return

	# Sets are a great way to reduce an algoritm that seems N ** 2, to N
	seen = set()
	output = set()

	for num in arr:

		target = k - num

		# Very useful and fast, as accessing is achieved with sets hashing
		if target not in seen:
			seen.add(num)
		else:
			# output.add( ((min(num, target)), max(num, target)) )
			output.add( ((min(num, target)), max(num, target)) )

	# return len(output)
	print('\n'.join(map(str, list(output))))

if __name__ == '__main__':
	pair_sum([1, 3, 2, 2, 1, 3, 2, 2, 1, 3], 4)



