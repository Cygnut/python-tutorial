
"""Some common katas in Python:
"""

"""Here's how 'Hello World!' is spelt in Python:
"""

# %%

print('Hello World!')

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
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
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
