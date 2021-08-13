"""Okay, about the indenting thing..

Python uses indentation to define blocks and scope, instead of curly braces. An indent
is defined as 4 spaces.
"""

# %%

x = 1
if x == 1:
    print("x is 1, well done.")

# %%

"""pass
You should use 'pass' in situations where a level of indentation is required to indicate the
termination of a block, but you have nothing useful to write. This is usually the case with
empty methods or classes, e.g.:
"""

# Just the following won't work - and result in a SyntaxError:
# def some_empty_function():

# %%

def some_empty_function():
    pass

# This happens all the time - wanting to specify a custom exception type, but not needing anything
# in the inherited class
class SomeCustomException(Exception):
    pass

# %%
