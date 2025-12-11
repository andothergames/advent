# --- Day 4: The Ideal Stocking Stuffer ---

import hashlib

# print(hashlib.md5(b"iwrupvqb").hexdigest())
# print(hashlib.md5(b"abcdef609043").hexdigest())


input = "iwrupvqb"
i = 0

while True:
    key = input + str(i)
    hash = hashlib.md5(key.encode()).hexdigest()

    if hash.startswith("000000"):
        print(i, key)
        break

    i += 1


