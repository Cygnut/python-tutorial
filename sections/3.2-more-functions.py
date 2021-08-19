"""Every function in Python receives a predefined number of arguments, if declared normally, like this:
"""

# %%


def some_function(first, second, third):
    pass


# %%

"""It is possible to declare functions which receive a variable number of arguments, using the
syntax below.
- *args must be placed after all positional arguments, and 'catches' all otherwise unspecified
positional arguments.
- It then places their values in a tuple named args.
- 'args' is the conventional name for such an argument.
"""

# %%


def foo(first, second, third, *args):
    print(f"First: {first}")
    print(f"Second: {second}")
    print(f"Third: {third}")
    print(f"And all the rest... {args}")


foo(1, 2, 3, 4, 5)

# %%

"""It is also possible to send functions arguments by keyword, so that the order of the argument
does not matter, using the syntax below.
- **kwargs must be placed after all keyword arguments, and 'catches' all otherwise unspecified
keyword arguments.
- It then places their values in a dict named kwargs.
- 'kwargs' is the conventional name for such an argument.
"""

# %%


def bar(first, second, third, **kwargs):
    if kwargs.get("action") == "sum":
        print(f"The sum is: {first + second + third}")

    if kwargs.get("number") == "first":
        print(first)


bar(1, 2, 3, action="sum", number="first")

# %%

"""Using *args and **kwargs
"""

# %%


def receive(apple, orange, *args, ham=1, eggs=True, **kwargs):
    print("Today I received:")
    print(f"apple={apple}")
    print(f"orange={orange}")
    print(f"args={args}")
    print(f"ham={ham}")
    print(f"eggs={eggs}")
    print(f"kwargs={kwargs}")


# The minimum number of argument required for a valid function call.
receive(1, 2)

# Using enough arguments to require *args and **kwargs to catch the excess
receive(1, 2, 3, 4, 5, ham=2, eggs=False, cheese="hell yes", lamb="hell no")

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
