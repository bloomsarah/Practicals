numbers = []

while len(numbers) < 5:
    number = float(input("Enter a number: "))
    numbers.append(number)

average = sum(numbers)/5

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(average))



