"""The defacto way to format strings nowadays (as is true in most languages), is to use string
interpolation - manifesting in Python as f-strings"""

name = 'bob'
age = 79

# Spot the difference between these two lines..
print("{name} is {age} years old.")
print(f"{name} is {age} years old.")