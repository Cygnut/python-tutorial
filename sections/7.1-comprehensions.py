"""list comprehensions are a very powerful tool, which creates a new list based on another list, in
a single, readable line.

For example, let's say we need to create a list of integers which specify the length of each word in
a certain sentence, but only if the word is not the word "the".
"""

# %%

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)

# %%

# Using a list comprehension, we could simplify this process to this notation:

# %%

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# %%

"""set comprehensions are pretty similar, you just swap [] for {}:
"""

# %%

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
unique_word_lengths = {len(word) for word in words if word != "the"}
print(unique_word_lengths)

# %%

"""dict comprehensions come along for the ride..
"""

# %%

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
words_with_lengths = {word: len(word) for word in words if word != "the"}
print(words_with_lengths)

# %%
