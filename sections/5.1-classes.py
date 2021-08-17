"""Classes & objects are an encapsulation of variables and functions into a single entity. Objects
get their variables and functions from classes. Classes are essentially a template to create your
objects.

A very basic class would look something like this:
"""

# %%


class Car:
    def method(self):
        print("Vroom vroooooooommmmmm...")


# %%

"""We'll explain why you have to include 'self' as a parameter a little bit later.

There's no 'new' - which is a really good thing - you don't need to worry about if the thing
you're using to create an object is a function or a constructor, which is a big help in things like
dependency injection & unit testing..

To instantiate a class instance:
"""

# %%

car = Car()
print(dir(car))
# help(car)

# %%

"""Why self?
There's no 'this' in Python, and the simplest way to think about this is how weird it is that 'this'
is a variable which isn't declared anywhere in other languages? It's just magically there. In
python, it is the first argument passed in all class methods, which refers to the current instance -
that's it.

As for naming - 'self' is the name, by convention, for that first argument. You could use anything (
use 'self' though, as linters know to look for and highlight that!)
"""

# %%


class Dog:
    def method(self):
        print("Woof")

    def weird_method(me, another_var):
        print(
            "Growl - you can do this, but don't - it's just to show there's nothing 'magic' about the word self"
        )
        print(another_var)
        me.method()


dog = Dog()
dog.method()
dog.weird_method("treat")

# %%

"""Why cls?
In 'class methods', which are methods associated with the class, rather than a specific instance,
the class itself is always passed as the first argument. Again, the name 'cls' is convention
rather than enforced.

To create a class method, the method must be attributed with @classmethod.
"""

# %%


class Aeroplane:
    @classmethod
    def class_method(cls, a, b, c):
        print(cls)
        return a + b + c


print(Aeroplane.class_method(1, 2, 3))

# %%

"""Accessing Member Data
To access the variable inside of the newly created object you would do the following:
(Don't worry about __init__ for now - we'll come back to that - just know that this is how you
create member data..)
"""

# %%


class Food:
    def __init__(self):
        self.flavour = "sweet"


food = Food()
print(food.flavour)

# %%

"""Accessing Methods
To access a function inside of an object you use the same syntax to accessing a variable:
"""

# %%


class Light:
    def switch_on(self, on):
        print(f"Switched {'on' if on else 'off'}")


light = Light()
light.switch_on(True)
light.switch_on(False)

# %%

"""__init__
__init__ may be thought of as the constructor in Python:
"""

# %%


class Toe:
    def __init__(self, type):
        self.type = type
        print(f"An instance of this class was instantiated with toe={self.type}")


toe = Toe("pinky")

# %%

"""Class vs instance data
Any data defined outside of a function is the equivalent of class static data. There is no such
thing as a member declaration in Python, so this is a place many people go wrong..
"""

# %%


class Person:
    planet = "earth"

    def __init__(self, name):
        self.name = name


people = [Person("alice"), Person("bob")]


def print_people(people):
    for person in people:
        print(person.name)
        print(person.planet)


# You'll see that name differs between instances, but planet does not..
print_people(people)

# Here's a way to check that Human.planet is 'static', i.e. scoped to the class, not the instance.
# Change it on one - and it changes it on both!
people[0].planet = "mars"

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


class Example:
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


example = Example()
print(example.public)
print(example.public_method())

print(example._private)
print(example._private_method())

try:
    print(example.__really_really_private)
except Exception as e:
    print(e)

try:
    print(example.__really_really_private_method())
except Exception as e:
    print(e)

print(dir(example))
# help(example)

# %%
