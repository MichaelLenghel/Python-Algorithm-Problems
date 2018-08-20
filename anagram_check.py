# Program that will check if two strings are anagrams, not including captials or spaces

from collections import defaultdict

# Has a time complexity of O(N), ideal for small data sets, but space complexity is of O(26). As 26 references are made from hashmap.
def anagram_chcek(s1, s2):

	# Sets the default value of all keys to zero
	ana_li = defaultdict(default_value)
	# Removes spaces in both strings
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()

	# If length isn't the same, then no way to be an anagram
	if len(s1) != len(s2):
		return False

	# Increment by one for each dictionary letter key every time a letter is incurred
	for letter in s1:
		ana_li[letter] += 1

	# Decrement respective keys incremented previously, return False if we have past zero.
	for letter in s2:
		if ana_li[letter] < 0:
			return False
		else:
			ana_li[letter] -= 1

	# If all values have not eached 0, return False, as imbalance of letters
	for letter in ana_li:
		if ana_li[letter] != 0:
			return False

	# Will return True if all checks pass
	return True

def default_value():
	return 0

# Has a time complexity of O(log n) since we use pythons built in timsort to arrange letters
def anagram_chcek_sorted(s1, s2):

	# Removes spaces in both strings
	s1 = s1.replace(" ", "").lower()
	s2 = s2.replace(" ", "").lower()

	# If length isn't the same, then no way to be an anagram
	if len(s1) != len(s2):
		return False
	else:
		return sorted(s1) == sorted(s2)

if __name__ == '__main__':
	s1 = "tram"
	s2 = "mart"
	if anagram_chcek(s1, s2):
		print("{} and {} are anagrams!".format(s1, s2))
	else:
		print("{} and {} are not anagrams!".format(s1, s2))

