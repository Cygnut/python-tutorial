"""Lists are very similar to arrays. They can contain any type of variable, and they can contain as
many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an
example of how to build a list.
"""

# %%

some_list = []
some_list.append(1)
some_list.append(2)
some_list.append(3)
print(some_list[0]) # prints 1
print(some_list[1]) # prints 2
print(some_list[2]) # prints 3

# prints out 1,2,3
for x in some_list:
    print(x)

# %%

"""Accessing an index which does not exist generates an exception (an error).
"""

# %%

some_list = [1,2,3]
try:
    print(some_list[10])
except Exception as e:
    print(e)

# %%

"""Lists of tuples are very useful, and can be unpacked in for-loops
"""

# %%

us_states = [
    ('alabama', 12, False),
    ('california', 50, True),
    ('texas', 70, False)
]

for state, votes, dem in us_states:
    print(f"{state} has around {votes} electoral college votes and they're pretty {'democratic' if dem else 'republican'}-leaning..")

# %%