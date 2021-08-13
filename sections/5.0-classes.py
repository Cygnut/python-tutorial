"""Objects are an encapsulation of variables and functions into a single entity. Objects get their
variables and functions from classes. Classes are essentially a template to create your objects.

A very basic class would look something like this:
"""

# %%

class SomeClass:
    variable = "blah"

    def method(self):
        print("This is a message inside the class.")

# %%

"""We'll explain why you have to include that "self" as a parameter a little bit later.
First, to assign the above class(template) to an object you would do the following:

There's no 'new' - which is a really good thing - you don't need to worry about if the thing
you're using to create an object is a function or a constructor, which is a big help in things like
dependency injection & unit testing..
"""

# %%

some_object = SomeClass()
print(dir(some_object))
#help(some_object)

# %%

"""Why self?
There's no 'this' in Python, and the simplest way to think about this is how weird it is that 'this'
is a variable which isn't declared anywhere, it's just magically there. Use 'self' though, as
linters know to look for that.

In Python, the first parameter passed to methods is by convention named 'self', and is bound to the
current instance.
"""

# %%

class SomeClass:
    variable = "blah"

    def method(self):
        print("This is a message inside the class.")

    def method2(me, another_var):
        print("You can do this, but don't - it's just to show there's nothing 'magic' about the word self")
        print(another_var)
        me.method()

some_class = SomeClass()
some_class.method()
some_class.method2('something')

# %%

"""Why cls?
In 'class methods', which are methods associated with the class, rather than a specific instance,
the class itself is always passed as the first argument. Again 'cls' is convention rather than
enforced.

To create a class method, the method should be attributed with @classmethod.
"""

# %%

class SomeClass:
    variable = "blah"

    @classmethod
    def class_method(cls, a, b, c):
        print(cls)
        return a + b + c

print(SomeClass.class_method(1, 2, 3))

# %%

"""Accessing Object Variables
To access the variable inside of the newly created object 'some_object' you would do the following:
"""

# %%

class SomeClass:
    variable = "blah"

    def method(self):
        print("This is a message inside the class.")

some_object = SomeClass()
some_object.variable

# %%

"""Accessing Object Functions
To access a function inside of an object you use notation similar to accessing a variable:
"""

# %%

class SomeClass:
    variable = "blah"

    def method(self):
        print("This is a message inside the class.")

some_object = SomeClass()
some_object.method()

# %%

"""__init__
__init__ may be thought of as the constructor in Python:
"""

# %%

class SomeClass:
    def __init__(self, toe):
        self.toe = toe
        print(f"An instance of this class was instantiated with toes={toe}")

some_object = SomeClass('pinky')

# %%

"""Class vs instance data
Any data defined outside of a function is the equivalent of class static data. There is no such
thing as a member declaration in Python, so this is a place many people go wrong in Python.
"""

# %%

class Person:
    planet = "earth"

    def __init__(self, name):
        self.name = name


people = [
    Person('alice'),
    Person('bob')
]

def print_people(people):
    for person in people:
        print(person.name)
        print(person.planet)

# You'll see that name differs between instances, but planet does not..
print_people(people)

# Here's a way to check that Human.planet is 'static', i.e. scoped to the class, not the instance.
# Change it on one - and it changes it on both!
people[0].planet = 'mars'

print_people(people)

# This is why class-level data is normally 'hidden' away, and not changed, apart from possibly
# for patching during unit testing.. But the 'standard' use would be for fixed data.

# %%

"""Public vs protected vs private
This is only enforced by convention, and name mangling:
- Data/functions starting with _ is as accessible as everything else - but by convention internal/
private.
- Data/functions on classes starting with __ (a 'dunder' or double-underscore) should *never* be
used, and will be name-mangled at runtime (which will lead to exceptions if you have attempted to use
it).
Python puts the trust on the developers, rather than enforcing access keywords (e.g. private,
protected)
"""

# %%

class SomeClass:
    def __init__(self):
        self.public = None
        self._private = None
        self.__really_really_private = None

    def public_method(self):
        return None

    def _private_method(self):
        return None

    def __really_really_private_method(self):
        return None

some_object = SomeClass()
print(some_object.public)
print(some_object.public_method())

print(some_object._private)
print(some_object._private_method())

try:
    print(some_object.__really_really_private)
except Exception as e:
    print(e)

try:
    print(some_object.__really_really_private_method())
except Exception as e:
    print(e)

print(dir(some_object))
#help(some_object)

# %%