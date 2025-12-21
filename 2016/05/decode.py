# --- Day 4: Security Through Obscurity ---

with open('0416input.txt', 'r') as file:
    data = file.readlines()


def formatData(data):
    codes = []
    for line in data:
        newLine = []
        line = line.rstrip().split('[')
        newLine.append(line[0])
        code = line[1][:-1]
        newLine.append(code)
        codes.append(newLine)
    return codes


def orderLetters(letters):
    orderedLetters = dict(sorted(letters.items(), key=lambda item: (-item[1], item[0])))
    return orderedLetters.keys()


def countChars(code):
    letters = {}
    ignore = ['0','1','2','3','4','5','6','7','8','9']
    for c in code:
        if c != '-' and c not in ignore:
            letters[c] = letters.get(c, 0) + 1
    return letters


def testKeys(keys, code):
    checker = True
    i = 0
    while i < len(code) - 1:
        if keys[i] != code[i]:
            checker = False
        i += 1
    return checker


def main(codes):
    total = 0
    for line in codes:
        countedChars = countChars(line[0])
        keys = list(orderLetters(countedChars))
        if testKeys(keys, line[1]):
            total += int(line[0][-3:])
    print(total)
    return total

        
codes = formatData(data)
main(codes)
