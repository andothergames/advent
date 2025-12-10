def makeNewString(s):
    result = []
    i = 0
    n = len(s)

    while i < n:
        count = 1
        while i + count < n and s[i] == s[i + count]:
            count += 1

        result.append(str(count))
        result.append(s[i])
        i += count

    return "".join(result)


def countDigits_iterative(s, steps=40):
    for _ in range(steps):
        s = makeNewString(s)
    return len(s)


def countDigits_recursive(s, steps=40):
    if steps == 0:
        return len(s)
    return countDigits_recursive(makeNewString(s), steps - 1)


print(countDigits_iterative("1113122113"))
print(countDigits_recursive("1113122113"))
