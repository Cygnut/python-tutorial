"""The 'with' keyword is generally used with unmanaged resources (files, streams, thread mutexes) to
ensure that a resource is cleaned up when you are done with it, however it finishes (e.g. if there's
an exception or not). Put another way, it's a 'better' try/finally.

    def unsafe_write_file():
        f = open('some_important_file.txt', 'a')
        f.write('some text')
        data = query_db_for_more_data()
        f.write_data(data)

unsafe_write_file has the following issue - if query_db_for_more_data() throws an exception,
then the file handle on 'some_important_file.txt' will never be released - a handle leak.

The safe way to write this function is:

    def safe_write_file():
        with open('some_important_file.txt', 'a') as f
            f.write('some text')
            data = query_db_for_more_data()
            f.write_data(data)

Now, whether query_db_for_more_data throws an exception or not, whenever the 'with' block is exited,
the file handle will be released.
"""

"""Here's an example of a custom class implementing the context manager protocol to support use in
the with statement - this isn't code you'd normally write, you'd normally just use 'with' with
objects provided by some package - but it simulates another good example, ensuring a database
connection is always disposed of regardless of errors in client code, to avoid wasting / DoS-ing
the db.
"""

# %%

class DatabaseConnection:

    def connect(self):
        print("Connecting to the database")
        # Database connection code...

    def disconnect(self):
        print("Disconnecting from the database")
        # Database disconnection code...

    def query(self, q):
        print("Running query")
        if not q:
            raise RuntimeError("Raising an exception because an empty query is considered an error")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

# Unsafe:

try:
    db = DatabaseConnection()
    db.connect()
    # Oops! This will throw, and we'll never disconnect - you can tell by looking for the printed
    # line saying 'Disconnecting from the database' - it won't be there!
    db.query('')
    db.disconnect()

except Exception as e:
    print(e)

# Safe:

try:
    # Now you'll see the connect and disconnect
    with DatabaseConnection() as db:
        db.query('')
except Exception as e:
    print(e)

# %%