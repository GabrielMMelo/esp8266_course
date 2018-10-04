import btree

class DB():
    def __init__(self):
        # First, we need to open a stream which holds a database
        # This is usually a file, but can be in-memory database
        # using uio.BytesIO, a raw flash partition, etc.
        # Oftentimes, you want to create a database file if it doesn't
        # exist and open if it exists. Idiom below takes care of this.
        # DO NOT open database with "a+b" access mode.
        try:
                f = open("myself.db", "r+b")
        except OSError:
                f = open("myself.db", "w+b")

                # Now open a database itself
                self.db = btree.open(f)

                # The keys you add will be sorted internally in the database
                self.db[b"3"] = b"three"
                self.db[b"1"] = b"one"
                self.db[b"2"] = b"two"

                # Assume that any changes are cached in memory unless
                # explicitly flushed (or database closed). Flush database
                # at the end of each "transaction".
                self.db.flush()
                self.db.close()

                # Don't forget to close the underlying stream!
                f.close()
