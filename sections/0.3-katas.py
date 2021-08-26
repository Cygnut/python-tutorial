"""Some common katas in Python:
"""

"""FizzBuzz:
Write a program that prints each of the numbers 1 - 100 on a new line - however..

    - If the number is a multiple of 3, print "Fizz" instead of the number.
    - If the number is a multiple of 5, print "Buzz" instead of the number.
    - If the number is a multiple of both 3 *and* 5, print "FizzBuzz" instead of the number.

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

"""Factorial:

The factorial function is defined in the following way:

    factorial(n) == n * (n - 1) * (n - 2) * ... * 1
    factorial(1) == 1
    factorial(0) == 1

Implement factorial for all non-negative integers, in the following ways:
    1. Using recursion
    2. Using a for-loop
    3. Using a lambda with reduce()
    4. Using the standard library

Which of these approaches do you prefer, and are there any pre-conditions you should be aware of
when using any of them?

Which do you think will be the fastest, and why?
"""

# %%

from functools import reduce
import math


def factorial_recursive(n):
    return n * factorial_recursive(n - 1) if n else 1


def factorial_looped(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def factorial_standard(n):
    return math.factorial(n)


factorials = (
    factorial_recursive,
    factorial_looped,
    factorial_reduce,
    factorial_standard,
)
for fn in factorials:
    for n in (0, 1, 10, 100):
        print(f"Using {fn.__qualname__}({n}), n! = {fn(n)}")


# A pre-condition of the recursive implementation is that it will fail after a point due to reaching
# the maximum recursion depth.

# This would work:
# print(factorial_looped(5000))

# This will crash out (comment out if you'd like to see this for yourself):
# print(factorial_recursive(5000))

from timeit import timeit

for factorial in factorials:
    qualname = factorial.__qualname__
    call = f"{qualname}(100)"
    print(f"Calling {call}")
    print(
        timeit(
            call,
            setup=f"from {__name__} import {qualname}",
            number=100,
        )
    )

# ..and if you have pandas installed:
# import pandas
# factorial_points = [ math.factorial(n) for n in range(1, 20) ]
# pandas.Series(factorial_points).plot.line()
# pandas.Series([ math.log10(f) for f in factorial_points ]).plot.line()


# %%

"""Prime sieves
Write an algorithm using the Sieve of Eratosthenes that will find all prime numbers between 1 and
10000.
"""

# %%


def eratosthenes(n):
    # We use a set rather than a list here as it's much faster when checking if i is in non_primes.
    non_primes = set()
    primes = []

    # Look at every number between 2 and n.
    for i in range(2, n + 1):

        # If we haven't already pre-determined that this is a non-primes, it has to be a prime.
        if i not in non_primes:

            # Add i to the list of primes.
            primes.append(i)

            # We then know all multiples of this prime between itself (i) and n are non-primes.
            #   However, we can improve upon this to reduce the number of add()s we need to do,
            # to make this a lot faster. We only need to look at i * i and n, as
            #  [ 2 * i, 3 * i, .. (i - 1) * i ] will have already been covered when we looked at
            # 2, 3, (i - 1) etc.
            for j in range(i * i, n + 1, i):
                non_primes.add(j)

    return primes


print(eratosthenes(10000))

from timeit import timeit

print(
    timeit(
        f"eratosthenes(10000)",
        setup=f"from {__name__} import eratosthenes",
        number=100,
    )
)

# ..and if you have pandas installed:
#
# import pandas
# pandas.DataFrame(eratosthenes(10000)).hist(bins=100)


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
