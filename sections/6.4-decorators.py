"""Decorators build on top of closures - they provide a way of sharing setup & teardown code - i.e.
the code at the start and end of a function.

The standard example is below, where we want to time how long a set of functions take to execute:
"""

from datetime import datetime
from time import sleep

def query_postgres_db(query):
    start = datetime.now()

    # Simulate a fast query to a postgres db
    print(query)
    sleep(0.5)
    print("Query ended successfully")

    end = datetime.now()
    print(f"query_mssqlserver_db took {end - start}")

def query_mssqlserver_db(query):
    start = datetime.now()

    # Simulate a slow query to a mssqlserver db
    print(query)
    sleep(2)
    print("Query ended successfully")

    end = datetime.now()
    print(f"query_mssqlserver_db took {end - start}")

query_postgres_db("SELECT * FROM DOGS")
query_mssqlserver_db("SELECT * FROM CATS")

# There's 2 types of duplication here:
# A) Code in the middle of the function;
# B) Code at the start at the end.
# Let's fix both!

# A) Well, we know how to resolve this, you just use a common function - as usual!

def _query(query, time_taken):
    print(query)
    sleep(time_taken)
    print("Query ended successfully")

def query_postgres_db(query):
    start = datetime.now()

    # Simulate a fast query to a postgres db
    _query(query, 0.5)

    end = datetime.now()
    print(f"query_mssqlserver_db took {end - start}")

def query_mssqlserver_db(query):
    start = datetime.now()

    # Simulate a slow query to a mssqlserver db
    _query(query, 2)

    end = datetime.now()
    print(f"query_mssqlserver_db took {end - start}")

query_postgres_db("SELECT * FROM DOGS")
query_mssqlserver_db("SELECT * FROM CATS")

# B) Hmmm - there's still a lot of duplication here - it'd be easy to eliminate if the code in the
# middle of the functions were duplicated (they could just call a common function), rather than the
# start and end. That's where decorators come in..

def time_me(func):
    def decorator(*args, **kwargs):
        start = datetime.now()
        # Ensure that any arguments passed to the actual function (rather than the decorator) are
        # forwarded
        result = func(*args, **kwargs)
        print(f"{func.__qualname__} took {datetime.now() - start}")
        # Ditto with the result of the function, we need to forward that too!
        return result
    return decorator

# Here's the same code as above, but using decorators:

@time_me
def query_postgres_db(query):
    _query(query, 0.5)

@time_me
def query_mssqlserver_db(query):
    _query(query, 2)

query_postgres_db("SELECT * FROM DOGS")
query_mssqlserver_db("SELECT * FROM CATS")

# Sweet!