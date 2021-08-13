"""Python uses boolean logic to evaluate conditions. The boolean values True and False are returned
when an expression is compared or evaluated. For example:
"""

# %%

x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# %%

"""Boolean operators
The "and" and "or" boolean operators allow building more complex boolean expressions, for example:
"""

# %%

name = "John"
age = 83
if name == "John" and age == 83:
    print("Your name is John, and you are also 83 years old.")

if name == "John" or name == "Wick":
    print("Your name is either John or Wick.")

# %%

"""The "in" operator
The "in" operator can be used to check if a specified object exists within an iterable object
container, such as a list:
"""

# %%

name = "John"
if name in [ "John", "Wick" ]:
    print("Your name is either John or Wick.")

# %%

"""The 'is' operator
Unlike the double equals operator "==", the "is" operator does not match the values of the
variables, but the instances themselves. For example:
"""

# %%

x = [ 1, 2, 3 ]
y = [ 1, 2, 3 ]
print(x == y) # Prints out True
print(x is y) # Prints out False

# %%

"""The "not" operator
Using "not" before a boolean expression inverts it:
"""

# %%

print(not False)
print((not False) == (False))

# %%

"""What's falsy?
In a conditional context, what's considered to be false?
"""

# %%

# Empty sequences
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(()))
print(bool(""))

# Zeroes
print(bool(0))
print(bool(0.0))
print(bool(0j))

# Booleans & None
print(bool(None))
print(bool(False))

# %%

"""The ternary expression
This is a little different to other languages, using the 'if' and 'else' keywords instead of ?:

The original logic behind it was to make it read more like human language.. I'm not so sure it
achieves that.. - but the fact that it uses existing symbols (if and else) rather than introducing
new ones for one specific purpose (? and :) is a better reason for it being like this.
"""

# %%

# In most languages you'd have
# true ? 'true' : 'false'
# But in python, we have:
print('true' if True else 'false')

# %%
