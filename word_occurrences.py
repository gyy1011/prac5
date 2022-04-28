word_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    number_of_times = word_count.get(word,0)
    word_count[word] = number_of_times + 1
words = list(word_count.keys())
words.sort()
length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word,length,word_count[word]))