"""Every function in Python receives a predefined number of arguments, if declared normally, like this:
"""

# %%


def some_function(first, second, third):
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
does not matter, using the following syntax.
"""

# %%


def bar(first, second, third, **kwargs):
    if kwargs.get("action") == "sum":
        print(f"The sum is: {first + second + third}")

    if kwargs.get("number") == "first":
        print(first)


bar(1, 2, 3, action="sum", number="first")

# %%

"""Functions (as with most definitions in Python) are first-class citizens, which is a big
simplification in a lot of situations..
"""

# %%


def old_function(num):
    return 10 * num


# Create an alias for new_function, for folks with ageism..
new_function = old_function

print(new_function(50) == old_function(50))

# Try and import a function, falling back it if it does not exist:
try:
    from os import some_non_existing_function
except ImportError:

    def some_non_existing_function():
        print(
            "Using the fallback, rather than something which doesn't exist in the os module"
        )


some_non_existing_function()
# %%
