"""Booleans
These are spelt False & True in Python. Yes it's weird.
"""

# %%

some_bool = False
print(some_bool)
some_bool = True
print(some_bool)

# %%

"""None
Python's None is similar to null in other languages, but it is strongly typed - with type 'NoneType'.
None is considered False in comparisons. Much like SQL, the Python standard recommends using the
'is' operator for comparison against None, rather than ==.
"""

# %%

its_none = None
print(its_none)
print(its_none is None)

# %%

"""Numbers
Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals).
(It also supports complex numbers, which will not be explained here).

To define an integer, use the following:
"""
# %%

some_int = 7
print(some_int)

# %%

"""To define a floating point number, you may use one of the following notations:
"""

# %%

some_float = 7.0
print(some_float)
some_float = float(7)
print(some_float)

# %%

"""Strings
Strings are most commonly defined either with a single quote or a double quotes.
.. but yes, a lot of the strings you're seeing right are here triple quotes..
"""

# %%

some_string = 'hello'
print(some_string)
some_string = "hello"
print(some_string)

# %%

"""The difference between the two is that using double quotes makes it easy to include apostrophes
(whereas these would terminate the string if using single quotes)
"""

# %%

some_string = "Don't worry about apostrophes"
print(some_string)

# %%

"""Simple operators can be executed on numbers and strings:
"""

# %%

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# %%

"""Assignments can be done on more than one variable "simultaneously" on the same line like this
This is really just tuple behaviour under the hood - there's no magic here.
"""

# %%

a, b = 3, 4
print(a,b)

# %%

"""Mixing operators between numbers and strings is not supported:
"""

# %%

# This won't work!
one = 1
two = 2
hello = "hello"

try:
    print(one + two + hello)
except Exception as e:
    print(e)

# %%
