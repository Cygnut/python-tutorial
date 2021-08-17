"""A closure is a function object that remembers values in enclosing scopes even if they are not
present in the immediate scope.

Closures are not 'new' to programming - we're just going to show what they look like in by python
in order to build towards decorators. 
"""

# %%


def make_closure(owner):
    callers = []
    # This is the enclosing function
    def the_closure(user):
        callers.append(user)
        # The nested function
        print(
            f"Hi {owner}, the closure has now been called by the following users: {', '.join(callers)}"
        )

    return the_closure


closure = make_closure("Top dog")
closure("alice horse")
closure("bob horse")
closure("charlie horse")

# %%

"""In javascript-land, the definition of `make_closure` would be the equivalent of:

function make_closure(owner) {
    let callers = [];
    return function(user) {
        callers.push(user)
        console.log(`Hi ${owner}, the closuer has now been called by the following users: ${callers.join(', ')}`);
    };
}
"""
