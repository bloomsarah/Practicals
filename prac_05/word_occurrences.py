# Make program to count the occurrences of words in a string
# ask user for a string
# print counts of how many of each word in the file
# use a dictionary where keys are words and values are counts

word_to_count = {}

words = input("Text: ")

frequency = word_to_count.get(word, 0)
unique_words[word] = frequency + 1       
        
for key, value in sorted(word_to_count.items()):
    print("{} : {}".format(key, value))


