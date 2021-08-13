"""A closure is a function object that remembers values in enclosing scopes even if they are not
present in memory.

Closures are not 'new' to python - they're just supported by it, they are everywhere in javascript
and in PHP (where non-local variables are specified in the use-block rather than implicit in
javascript).
"""

# %%

def make_closure(owner):
    callers = []
    # This is the enclosing function
    def the_closure(user):
        callers.append(user)
        # The nested function
        print(f"Hi {owner}, the closure has now been called by the following users: {', '.join(callers)}")

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
