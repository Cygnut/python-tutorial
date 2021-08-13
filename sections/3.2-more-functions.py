"""Every function in Python receives a predefined number of arguments, if declared normally, like this:
"""

# %%

def some_function(first, second, third):
    # do something with the 3 variables
    ###...
    pass

# %%

"""It is possible to declare functions which receive a variable number of arguments, using the
following syntax:
"""

# %%

def foo(first, second, third, *args):
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Third: {third}")
    print(f"And all the rest... {list(args)}")

foo(1, 2, 3, 4, 5)

# %%

"""It is also possible to send functions arguments by keyword, so that the order of the argument
does not matter, using the following syntax. The following code yields the following output: The sum
is: 6 Result: 1
"""

# %%

def bar(first, second, third, **kwargs):
    if kwargs.get("action") == "sum":
        print(f"The sum is: {first + second + third}")

    if kwargs.get("number") == "first":
        print(first)

bar(1, 2, 3, action = "sum", number = "first")

# %%