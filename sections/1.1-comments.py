"""Single line comments start with a #, like SQL & PHP (kinda..)
"""

# this is a single line comment

"""Multi-line comments
The equivalent of a multi-line comment in Python is to embed multi-line strings, using the triple-quote 
syntax (e.g. right here!).

This syntax is also used for doc-block comments, which most editors support, and has language support via
the __doc__ attribute.

Try hovering over the function below with your mouse!
"""

# %%

def talkative():
    """talkative loves to talk about himself
    """
    print('I am talkative')
    return None

print(talkative.__doc__)

# %%
