"""sets are like dicts mashed up with lists:
- Every item appears only once uniquely.
- They are unordered and unindexed
"""

# Even though we construct the set with the value '1' specified multiple times, the constructed
# object only contains it once.
some_set = {1, 2, 4, 5, 1, 1, 1, 1}
print(some_set)

"""Because they're intrincally hashed, as with dicts - they're super-fast for find operations, much
faster than a list, but generally slower to modify.
"""

from timeit import timeit

def iter_test(iterable):
    candidate = 10000
    if candidate in iterable:
        print(f"Found {candidate}")

for collection in [ 'set', 'list' ]:
    number=100000
    print(f"When using a {collection}, {number} iterations..")
    timeit(
        "iter_test(iterable)",
        setup=f"from {__name__} import iter_test; iterable = {collection}(range(10000))",
        number=number
    )