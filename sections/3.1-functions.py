"""Functions in python are defined using the keyword "def", followed with the function's name
as the block's name. For example:
"""

# %%

def some_function():
    print("Hello from some_function!")

some_function()

# %%

"""Functions may also receive arguments (variables passed from the caller to the function). For
example:
"""

# %%

def some_function_with_args(username, greeting):
    print(f"Hello, {username} , from some_function!, I wish you {greeting}")

some_function_with_args('tomdog', 'a good day')

# %%

"""Functions may return a value to the caller, using the keyword - 'return' . For example:
"""

# %%

def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(1, 2))

# %%

""" Keyword Arguments """

"""Why use keyword arguments?
When calling functions in Python, you’ll often have to choose between using keyword arguments or
positional arguments. Keyword arguments can often be used to make function calls more explicit.

Take this code:
"""

# %%

def write_gzip_file(output_file, contents):
    with GzipFile(None, 'wt', 9, output_file) as gzip_out:
        gzip_out.write(contents)

# %%

"""This takes a file object output_file and contents string and writes a gzipped version of the
string to the output file.
This code does the same thing but it uses keyword arguments instead of positional arguments:
"""

# %%

def write_gzip_file(output_file, contents):
    with GzipFile(fileobj=output_file, mode='wt', compresslevel=9) as gzip_out:
        gzip_out.write(contents)

# %%

"""Notice that using this keyword argument call style made it more obvious what each of these
three arguments represent.

We were also able to leave off an argument here. The first argument that we left off represents a
filename and already has a default value of None. We don’t need a filename here because we’re
supposed to pass either a file object or a filename to GzipFile, not both.

We’re actually able to leave another argument off though.

Here’s the same code again, but the compress level has been left at its default value of 9 this time:
"""

# %%

def write_gzip_file(output_file, contents):
    with GzipFile(fileobj=output_file, mode='wt') as gzip_out:
        gzip_out.write(contents)

# %%

"""
Because we used named arguments, we were able to leave out two arguments and rearrange the remaining
2 arguments in a sensible order (the file object is more important than the "wt" access mode).

When we use keyword arguments:

- We can often leave out arguments that have default values
- We can rearrange arguments in a way that makes them most readable
- We call arguments by their names to make it more clear what they represent
"""

"""Problems with keyword/default arguments
In Python, defaults arguments are only instantiated once - this creates issues if these are modified
during function calls:
"""

# %%

def append_to_list_buggy(a, initial_list=[]):
    initial_list.append(a)
    return initial_list

# We expect all of the following to return a list containing a single item.. but they won't..
print(append_to_list_buggy(1))
print(append_to_list_buggy(2))
print(append_to_list_buggy(3))

# %%

"""There's two ways around this which are usually used:
- Not modifying mutable parameters
- Using a sentinel to indicate a new instantiation should occur
"""

# %%

def append_to_list_fixed(a, initial_list=None):
    initial_list = initial_list or []
    initial_list.append(a)
    return initial_list

print(append_to_list_fixed(1))
print(append_to_list_fixed(2))
print(append_to_list_fixed(3))

# %%
