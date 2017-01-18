from nltk.tokenize import sent_tokenize, word_tokenize

def word(sentence):
	
	word_sent = word_tokenize(sentence)
	# words = sentence.split('')

	# set for tracking
	seen = set()
	output = {}

	for word in word_sent:
		if word not in seen:
			seen.add(word)
			output[word] = 1
		else:
			output[word] += 1

	return output

	


if __name__ == '__main__':
	print(word('GO    go   go 1 2 3 1'))