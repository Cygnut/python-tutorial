"""Tuples are fixed length collections, they are mainly used to store many items in a single
variable. They are 'frozen' after construction, which means they cannot be altered.

They can be unpacked as required.
"""

some_tuple = (1, 2, 4)
print(some_tuple)
a, b, c = some_tuple
print(a)
print(b)
print(c)

"""They can be unpacked if required
"""
a, b, c = some_tuple
print(a)
print(b)
print(c)

"""A tuple of 1 item looks a bit weird:
"""

tuple_of_one = (1,)
print(tuple_of_one)
one, = tuple_of_one
print(one)

"""A tuple of 0 items is a bit weirder - you have to use parentheses:
"""

tuple_of_zero = ()
print(tuple_of_zero)

"""One handy thing to keep in mind is that it's the comma (,) which makes it a tuple, not the
parentheses (though these can help for clarification). One exception to this rule is with a tuple
with zero items
"""

no_parens = 1, 2, 3
with_parens = (1, 2, 3)
print(with_parens == no_parens)

no_parens = 1,
with_parens = (1,)
print(with_parens == no_parens)
