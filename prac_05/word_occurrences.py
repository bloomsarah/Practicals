# Make program to count the occurrences of words in a string
# ask user for a string
# print counts of how many of each word in the file
# use a dictionary where keys are words and values are counts

word_to_count = {}

words = input("Text: ")

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
for key, value in word_to_count.items():
    print("Word: ", key, "appears", value, "times.")


#This is currently counting each letter as it's own word yikes how to fix??