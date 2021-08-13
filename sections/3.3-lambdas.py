"""Lambdas - these are essentially short, anonymous functions as available in other languages. A
lambda in python may only consist of a single line. One of the most useful places where lambdas are
used are in comprehensions - but there the lambda keyword isn't even used!
"""

adder = lambda x: x + 1
print(3 == adder(2))

"""Lambdas can always be replaced by a reference to an existing function, so they're not crucial -
we'll see this below.
"""

def longer_adder(x):
    return x + 1

print(3 == longer_adder(2))

"""Implicit lambdas in comprehensions
This will be covered in a later section, but for completeness, here's an example:
"""

entities = [
    'alsatian dog',
    'siamese cat',
    'big hat logan'
]

# Here, `a.upper()` would be the implicit lambda
uppered_entities = [ a.upper() for a in entities ]
print(uppered_entities)