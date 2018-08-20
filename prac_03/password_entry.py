def main():

    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    for char in password:
        print('*', end=' ')


def get_password():
    min_length = 10
    password = input("Enter a password: ")
    if len(password) < min_length:
        print("Invalid password!")
        password = input("Enter a password: ")
    return password


main()
