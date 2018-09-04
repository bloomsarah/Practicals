"""Program to take string input and count occurrences of each word
Sarah Bloom
3/9/18"""
word_to_count = {}

words = input("Text: ").split(' ')

for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

for key, value in sorted(word_to_count.items()):
    print("{} : {}".format(key, value))


