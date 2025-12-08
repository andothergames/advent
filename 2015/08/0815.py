# --- Day 8: Matchsticks ---

with open('0815input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]


def countCodeChars(data):
    codeCount = 0
    for line in data:
        for char in line:
            codeCount+= 1
    print(codeCount)
    return codeCount


def countStringChars(data):
    stringCount = 0
    for line in data:
        stringCount += resolveEscapedChars(line)
    print(stringCount)
    return stringCount


def resolveEscapedChars(str):
    s = list(str)
    total = 0
    i = 0
    while i < len(s):

        if s[i] == '\"':
            if i == 0 or i == len(s) - 1:
                i += 1
                continue
            total += 1
            i += 1
            continue
        if s[i] == '\\' and s[i+1] == '\\':
            total += 1
            i += 2
            continue
        if s[i] == '\\' and s[i+1] == '\"':
            total += 1
            i += 2
            continue
        if s[i] == '\\' and s[i+1] == 'x':
            total += 1
            i += 4
            continue
        total += 1
        i += 1
    return total


def findTotal(data):
    total = countCodeChars(data) - countStringChars(data)
    print(total)


findTotal(data)