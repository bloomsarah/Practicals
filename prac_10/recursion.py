"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        print(0)
    else:
        print(n ** 2)
        do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# TODO: 4. use the debugger to step through and see what's actually happening
print(do_something(4))

# TODO: 5. fix do_something() so that it works according to the docstring


def calculate_blocks(n):
    """Simple loop to calculate blocks for pyramid with number of rows n"""
    blocks = 0
    for i in range(n):
        blocks += n - i
    return blocks

print(calculate_blocks(6))


def calculate_blocks_recursive(n):
    if n <= 0:
        return 0
    return n + calculate_blocks_recursive(n - 1)

print(calculate_blocks_recursive(6))
