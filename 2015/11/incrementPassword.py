# --- Day 11: Corporate Policy ---


import string
input = 'cqjxjnds'

string.ascii_lowercase

alpha = list(string.ascii_lowercase)


# password requirement functions

def includesIncreasingSet(str):
    indexes = []
    n = 0
    for letter in str:
        i = alpha.index(letter)
        indexes.append(i)
    while n < len(indexes) - 2:
        if indexes[n] + 1 == indexes[n + 1] and indexes[n] + 2 == indexes[n + 2]:
            return True
        n += 1
    return False


def includesIncreasingSet(s):
    for i in range(len(s) - 2):
        if (
            ord(s[i+1]) == ord(s[i]) + 1 and
            ord(s[i+2]) == ord(s[i+1]) + 1
        ):
            return True
    return False


def excludesIOL(str):
    return 'i' not in str and 'o' not in str and 'l' not in str


def includesPairs(str):
    length = len(str) - 1
    x = 0
    pairs = 0
    while x < length:
        if str[x] == str[x + 1]:
            pairs += 1
            x += 2
            continue
        x += 1
    return pairs >= 2


def passing(str):
    return includesIncreasingSet(str) and excludesIOL(str) and includesPairs(str)


# increment function

def increment(password):
    password = list(password)

    i = len(password) - 1
    while i >= 0:
        if password[i] == 'z':
            password[i] = 'a'
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break

    return ''.join(password)

def main(code):
    password = code
    is_passing = False
    while is_passing == False:
        password = increment(password)
        is_passing = passing(password)
        if is_passing == True:
            return password
        

print(main(input))