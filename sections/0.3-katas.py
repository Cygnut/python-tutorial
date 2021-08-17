"""Some common katas in Python:
"""

"""Here's how 'Hello World!' is spelt in Python:
"""

# %%

print("Hello World!")

# %%

"""Factorial:
Implement this using recursion and imperitively.
"""

# %%

from functools import reduce


def factorial_recursive(n):
    return n * factorial_recursive(n - 1) if n else 1


def factorial_looped(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


for fn in [factorial_looped, factorial_recursive]:
    for n in [0, 1, 10, 100]:
        print(f"Using {fn.__qualname__}({n}), n! = {fn(n)}")


# The advantage of a loop is that the recursive implementation will fail after a point due to
# reaching the maximum recursion depth.

# This would work:
# print(factorial_looped(5000))

# This will crash out (comment out if you'd like to see this for yourself):
# print(factorial_recursive(5000))

# %%

"""FizzBuzz:
Write a program that prints the numbers 1-100, each on a new line.
- For each number that is a multiple of 3, print "Fizz" instead of the number.
- For each number that is a multiple of 5, print "Buzz" instead of the number.
- For each number that is a multiple of both 3 and 5, print "FizzBuzz" instead of the number.
"""

# %%


def fizzbuzz():
    for i in range(1, 101):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        print(s if s else i)


fizzbuzz()

# %%

"""Pythagoras:
Given a pair of points in a 2D space, compute the distance between them.
As an example, (0, 0) to (3, 4) should return 5.
"""

# %%


def pythagoras(p1, p2):
    xdiff = p1[0] - p2[0]
    ydiff = p1[1] - p2[1]
    return (xdiff ** 2 + ydiff ** 2) ** 0.5


print(pythagoras((0, 0), (3, 4)))

# %%

"""Bonus: n-dimensional Pythagoras:
"""

# %%

import itertools


def npythagoras(p1, p2):
    return (
        sum([(i1 - i2) ** 2 for (i1, i2) in itertools.zip_longest(p1, p2, fillvalue=0)])
        ** 0.5
    )


print(npythagoras((1, 2, 3, 4), (5, 6, 7, 8)))
print(npythagoras((0, 0, 0, 0), (0, 0, 3, 4)))

# %%

"""Newton-Rhapson:
How many iterations of the Newton-Rhapson method are required to approximate the square
root of 2 to 16 decimal places?
"""

# %%

import math


def sqrt(rootee, iterations):
    for i in range(iterations):
        rootee = rootee - (rootee ** 2 - 2) / 2
    return rootee


def compute_iterations_required():
    iterations = 1
    actual_value = 2 ** 0.5
    while True:
        approximated_value = sqrt(2, iterations)
        if math.fabs(approximated_value - actual_value) < 1.0e-16:
            return (iterations, approximated_value, actual_value)

        iterations += 1


iterations, approximated_value, actual_value = compute_iterations_required()
print(
    f"It will take {iterations} iterations to reach the actual value of {actual_value}, where we will approximate it with value {approximated_value}"
)

# %%
