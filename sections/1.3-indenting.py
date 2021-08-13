"""Yes, this thing..

Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported,
but the standard indentation requires standard Python code to use four spaces. For example:
"""

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

"""pass
You should use pass when in situations where a level of indentiation is required to indicate the
termination of a block, but you have nothing useful to write. This is usually the case with
empty methods or classes, e.g.:
"""

# Just the following won't work - and result in a SyntaxError:
# def some_empty_function():

def some_empty_function():
    pass

# This happens all the time - wanting to specify a custom exception type, but not needing anything
# in the inherited class
class SomeCustomException(Exception):
    pass
