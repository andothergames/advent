# --- Day 10: Elves Look, Elves Say ---


def makeNewString(str):
    l = list(str)
    length = len(l)
    nextl = []
    i = 0
    while i < length - 2:
        if l[i] != l[i + 1]:
            nextl.append('1')
            nextl.append(l[i])
            i += 1
            continue
        if l[i] == l[i + 1] and l[i] == l[i + 2] and l[i] != l[i + 3]:
            nextl.append('3')
            nextl.append(l[i])
            i += 3
            continue
        if l[i] == l[i + 1] and l[i] != l[i + 2]:
            nextl.append('2')
            nextl.append(l[i])
            i += 2
            continue
    end = dealWithEnd(l[length - 3], l[length - 2], l[length - 1])
    return ("").join(nextl + end)


def dealWithEnd(a, b, c):
    list = []
    if a == b and a != c:
        list.append('1')
        list.append(c)
        return list
    if a != b and b != c:
        list.append('1')
        list.append(b)
        list.append('1')
        list.append(c)
        return list
    if a != b and b == c:
        list.append('2')
        list.append(b)
        return list


def countDigits(input):
    i = 0
    string = input
    while i < 40:
        nextString = makeNewString(string)
        string = nextString
        i += 1
    return len(nextString)


print(countDigits('1113122113'))