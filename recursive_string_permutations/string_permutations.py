# Given a string, use recursion to output a list of all the possible permutations of a string
# If a character is repeated, treat all versions as distinct
# Itertools does permutations
def permute(s):
	out = []

	# Base case is when there is only one letter
	if len(s) < 2:
		out = [s]
	else:
		# For every letter in string
		for i, letter in enumerate(s):
			# For every permutation resultingfromstep2 a nd3
			for perm in permute(s[:i] + s[i+1:]):
				# add it to the output
				out += [let+perm]

	return out

s = "abc"
print(permute(s))