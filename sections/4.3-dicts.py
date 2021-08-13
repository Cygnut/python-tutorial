"""A dict is a data type similar to arrays, but works with keys and values instead of indexes.
Each value stored in a dict can be accessed using a key, which is any type of object (a string,
a number, a list, etc.) instead of using its index to address it.
For example, a database of phone numbers could be stored using a dict like this:
"""

# %%

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# %%

"""Alternatively, a dict can be initialized with the same values in the following notation:
"""

# %%

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(phonebook)

# %%

"""Iterating over dict
dicts can be iterated over, just like a list. However, a dict, unlike a list, does not
keep the order of the values stored in it. To iterate over key value pairs, use the following syntax:
"""

# %%

phonebook = {
    "John": 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
for name, number in phonebook.items():
    print(f"Phone number of {name} is {number}")

# %%

"""Removing a value
To remove a specified index, use either one of the following notations:
"""

# %%

phonebook = {
   "John": 938477566,
   "Jack": 938377264,
   "Jill": 947662781
}
del phonebook["John"]
print(phonebook)

# %%

# or..

# %%

phonebook = {
   "John": 938477566,
   "Jack": 938377264,
   "Jill": 947662781
}
phonebook.pop("John")
print(phonebook)

# %%

"""Tuples can be used as dict-keys, which is very useful
"""

# %%

locations_by_lat_lng = {
    (13.12341422, 59.45235234): "Guildford",
    (95.94535242, 55.09235782): "Vancouver",
    (65.12341452, 33.04985283): "New Zealand"
}
print(locations_by_lat_lng)

"""And here's a fun example of two types of argument unpacking happening:
"""
for (lat, lng), location in locations_by_lat_lng.items():
    print(f"My dad's summer home is in {location} so aim your nukes at ({lat}, {lng})")

# %%