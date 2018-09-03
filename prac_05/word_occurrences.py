"""Program to take string input and count occurrences of each word
Sarah Bloom
Prac_05
3/9/18"""
word_to_count = {}

words = input("Text: ")

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

for key, value in sorted(word_to_count.items()):
    print("{} : {}".format(key, value))


