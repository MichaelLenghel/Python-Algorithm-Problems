# Problem: Given three tuples and a string. Each tuples contains a word it will be using to replace parts of a string. An index of the word it is replacing and the actual
# word we are replacing in the string.

# e.g. tup1 contains: tup1[0] = Word we will be using to replace. tup[1] = index where replacing. tup[2] = String replacing.
#  Will return themodified string
def patches(s, tup1, tup2, tup3):
	# Edge case: Will need to append the new strings from the last index to the first. As if replace from the start it will change the index from the other words.
	# Edge case: Empty string, word not found, index out of bounds.

	# Encapsulate index values and associated tuple lists in an ordered list
	ordered = [(tup1[1], tup1), (tup2[1], tup2), (tup3[1], tup3)]
	# Sort the tuples in reverse order based on the index to eliminate the edge case of inserting at the start and the index changing for other tuples.
	ordered = sorted(ordered, reverse=True, key = lambda index: index[0])

	for index, tup in ordered:
		# Account for word not being in string and index being out of bounds
		if tup[2] in s and index < len(s) and index > 0:
			# end str will start from index + len(word) so will be right after the word we are replacing
			end_str = s[index - 1 + len(tup[2]):]
			# Word before index is not mofified. tup[0] will be word we are adding + end_str holds everything after word we are replacing
			s = s[:index - 1] + tup[0] + end_str
		else:
			return "One tuple did not contain all values or index range was out of bounds"

	return s


s = "The man walked througho the room"
tup1 = ("people", 5, "man")
tup2 = ("ut", 24, "")
tup3 = ("house", 29, "room")

new_str = patches(s, tup1, tup2, tup3)
# "The man walked through the room"
print("Initial string: \n{}\n".format(s))
# "The people walked through the house"
print("String after applying patch:\n{}\n".format(new_str))