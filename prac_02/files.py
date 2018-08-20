# Names file
name_file = open('name.txt', 'w')
name = input("Enter your name: ")
print(name, file=name_file)
name_file.close()

# Name reader
name_file = open('name.txt', 'r')
name_str = name_file.readline()
print("Your name is {}".format(name_str))

# Numbers file
number_file = open('numbers.txt', 'r')
