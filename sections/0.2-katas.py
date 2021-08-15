
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
