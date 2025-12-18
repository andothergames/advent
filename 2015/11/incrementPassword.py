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
    length = len(str) - 2
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
    letterIndex = alpha.index(password[-1])
    password[-1] = alpha[(letterIndex + 1) % 26]
    letter = -1

    while letter >= -len(password):
        if password[letter] == alpha[25]:
            password[letter] = alpha[0]
            if letter - 1 >= -len(password):
                prevIndex = alpha.index(password[letter - 1])
                password[letter - 1] = alpha[(prevIndex + 1) % 26]
        letter -= 1

    if password[0] == alpha[25]:
        password[0] = alpha[0]
    
    return "".join(password)



def main(code):
    password = code
    is_passing = False
    while is_passing == False:
        password = increment(password)
        is_passing = passing(password)
        if is_passing == True:
            return password
        

print(main(input))