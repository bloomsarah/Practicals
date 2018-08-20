MIN_LENGTH = 10

password = input("Enter a password: ")

if len(password) < MIN_LENGTH:
    print("Invalid password!")
    password = input("Enter a password: ")
else:
    for char in password:
        print('*', end=' ')
print()