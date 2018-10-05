import btree

#TODO Clean the code (avoid repetitions?)!
#TODO Clean blank lines (it's memory limited device) 

# First, we need to open a stream which holds a database
# This is usually a file, but can be in-memory database
# using uio.BytesIO, a raw flash partition, etc.
# Oftentimes, you want to create a database file if it doesn't
# exist and open if it exists. Idiom below takes care of this.
# DO NOT open database with "a+b" access mode.
def create():
    try:
            f = open("mydb", "r+b")

    except OSError:
            f = open("mydb", "w+b")

            # Now open a database itself
            db = btree.open(f, pagesize=512)

            # The keys you add will be sorted internally in the database
            db[b"3"] = b"three"
            db[b"1"] = b"one"
            db[b"2"] = b"two"

    # Assume that any changes are cached in memory unless
    # explicitly flushed (or database closed). Flush database
    # at the end of each "transaction".
    db.flush()
    db.close()
 
    # Don't forget to close the underlying stream!
    f.close()

def select(key):
    try:
            f = open("mydb", "r+b")
            db = btree.open(f, pagesize=512)

            try:
                value = db[key]
                db.close()
                f.close()
                return value

            except ValueError:
                print("Key not found")

                db.close()
                f.close()

    except OSError:
            print ("DB isn't initizalized")


    
def insert(key, value):
    try:
            f = open("mydb", "r+b")
            db = btree.open(f, pagesize=512)

            try:
                # TODO verify if key already exists
                db[key] = value

            except OSError:
                print("Disk is full")

            db.flush()
            db.close()
            f.close()

    except OSError:
            print ("DB isn't initizalized")

def list():
    try:
            f = open("mydb", "r+b")
            db = btree.open(f, pagesize=512)

            for key in db:
                print(key + ": " + db[key])
        
            db.close()
            f.close()

    except OSError:
            print("Database isn't initialized")

def delete(key):
    try:
            f = open("mydb", "r+b")
            db = btree.open(f, pagesize=512)
            
            try:
                del db[key]

            except ValueError:
                print("Key not found")

            db.flush()
            db.close()
            f.close()

    except OSError:
            print("Database isn't initialized")
