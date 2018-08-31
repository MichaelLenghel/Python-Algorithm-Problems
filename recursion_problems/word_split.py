"""
Create a function called word_split() which takes in a string phrase and a set list_of_words.
The function will then determine if it is possible to split the string in a way in which words can be made from the list of words.
Can assume the phrase will only contain words found in the dictionary if it is completely splittable.

For example:

Input: word_split('themanran',['the','ran','man'])
output: ['the', 'man', 'ran']
Input: word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
output: ['i', 'love', 'dogs', 'John']
Input: word_split('themanran',['clown','ran','man'])
output: []
"""

# Not accounting for a phrase having multiple of the same word
def word_split(phrase, list_of_words, output = None):

	# Cannot initialise to output = [] as gets redone everytime
	if output is None:
		output = []

	# If a word is findable, add it to the list and remove it from the phrase using the length of the word
	for word in list_of_words:
		# if word.startswith(phrase)
		# if word == phrase[:len(word)]:
		if word in phrase:
			output.append(word)
			# Remove word from phrase
			phrase = phrase.replace(word, "")
			# returning word in list that matches + phrase and list_of words with word gone
			return word_split(phrase, list_of_words, output)

	if phrase == "":
		return output
	else:
		return "Not all words in phrase are in the list" 


print(word_split('themanran',['the','ran','man']))
