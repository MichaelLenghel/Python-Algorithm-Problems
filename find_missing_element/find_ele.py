# Pass two arrays. First one has all the elements. 
# Second one has its elements shuffeled and one removed.
# Find which element is missing as efficiently as possible.

# What if it has duplicate values
from random import sample

def finder(li_full, li_missing):
	count = {}
	# Assign each value from li_missing as a key to the list
	for num in li_missing:
		# Need to say this, as we don't know if this has been previously set to 1
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





if __name__ == '__main__':
	li_full = [5, 16, 23, 77, 22, 9, 10, 22]
	li_shufled = sample(li_full, len(li_full))
	print(li_full)
	li_shufled.pop(2)
	print(li_shufled)
	missing_ele = finder(li_full, li_shufled)

	print("Missing element is {}".format(missing_ele))