"""
Create a function called word_split() which takes in a string phrase and a set list_of_words.
The function will then determine if it is possible to split the string in a way in which words can be made from the list of words.
Can assume the phrase will only contain words found in the dictionary if it is completely splittable.

For example:

Input: word_split('themanran',['the','ran','man'])
output: "Phrase is completely splitable"
Input: word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
output: "Phrase is completely splitable"
Input: word_split('themanran',['clown','ran','man'])
output: "Phrase cannot be split completely using the list_of_words"
"""

def word_split(phrase, list_of_words, output = None):
	if output == None:
		output = []

	for word in list_of_words:
		# if word.startswith(phrase)
		# if word == phrase[:len(word)]:
		if word in phrase:
			phrase = phrase.replace(word, "")
			word_split(phrase, list_of_words, output.append(word))

	return "".join(output)


def check_if_splitable(word_split, phrase):
	if len(word_split) == len(phrase):
		print("Phrase is completely splitable")
	else:
		print("Phrase cannot be split completely using the list_of_words")




phrase = 'themanran'
# Works
check_if_splitable(word_split(phrase, ['the', 'ran', 'man']), phrase)


# Wont work
check_if_splitable(word_split(phrase, ['clown', 'ran', 'man']), phrase)