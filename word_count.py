def words(string_of_words):
    word_sent = string_of_words.split()
    
    # set for tracking
    seen = set()
    output = {}
    
    for word in word_sent:
        if word not in seen:
            seen.add(word)
            if word.isdigit() is True:
              output[int(word)] = 1
            else:
              output[word] = 1
        else:
            if word.isdigit() is True:
              output[int(word)] += 1
            else:
              output[word] += 1
    
    return output


if __name__ == '__main__':
	print(words('testing 1 2 testing'))