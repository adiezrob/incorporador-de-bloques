import hashlib

def hash(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        digest = hashlib.sha256(bytes).hexdigest()
    return digest

fn = input("Name: ")
print(hash(fn))