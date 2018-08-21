# Reverse a sentence and get rid of all extended characters at the start and in the middle

def rev_word(s):
	s = s.split()
	return ' '.join(reversed(s))

def rev_word_2(s):
	words = []
	length = len(s)
	space = ' '

	i = 0

	while i < length:
		if s[i] != space:
			word_start = i

			while i < length and s[i] != space:
				i += 1
			# Uses string slicing to append in string from the start of the word to the end
			words.append(s[word_start:i])
		i += 1

	return " ".join(reversed(words))

# Alternative reverse method for fun:
# def reverse_words(words):
# 	print("list ", words)
# 	len_list = len(words) - 1
# 	i = 0
# 	words_reversed = ""
# 	while i != len(words) - 1:
# 		words_reversed += words[len_list - i] + " "
# 		i += 1
# 	words_reversed += words[0]
# 	return words_reversed

if __name__ == '__main__':
	sen = "       This is a sentence to           be reversed         "
	rev_sen = rev_word(sen)
	print("Normal sentence: ", sen)
	print("Reversed sentence: ", rev_sen)