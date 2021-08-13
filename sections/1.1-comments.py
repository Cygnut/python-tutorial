"""Single line comments start with a #, like SQL & PHP (kinda..)
"""

# this is a single line comment

"""Multi-line comments - there isn't any supported syntax for multi-line comments!
The convention is to jsut embed multi-line strings, using the triple-quote syntax (e.g. right here!).
This syntax is also the convention for docblock comments, which most editors support.
"""

def talkative():
    """talkative loves to talk about himself
    """
    print('I am talkative')
    return None

print(talkative.__doc__)