# --- Day 11: Corporate Policy ---

import string
input = 'cqjxjnds'

string.ascii_lowercase
alpha = list(string.ascii_lowercase)
alpha.append('#')


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


def excludesIOL(str):
    return 'i' not in str and 'o' not in str and 'l' not in str


def includesTwoPlusPairs(str):
    length = len(str) - 3
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
    return includesIncreasingSet(str) and excludesIOL(str) and includesTwoPlusPairs(str)


# increment function

def increment(password):
    letterIndex = alpha.index(password[-1])
    password[-1] = alpha[letterIndex]
    letter = -1

    while letter > 0 - len(password):
        if password[letter] == alpha[26]:
            password[letter] = 0
            password[letter - 1] += 1
        letter -= 1

    if password[0] == alpha[26]:
        password[0] = alpha[0]
    
    print(password)



def main(code):
    password = code
    passing = False
    while passing == False:
        password = increment(password)
        passing = passing(password)
        if passing == True:
            return password

