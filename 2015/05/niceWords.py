# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# part one

with open('0515input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

def checkNoPairs(x):
    if ('ab' in x):
        return False
    if ('cd' in x):
        return False
    if ('pq' in x):
        return False
    if ('xy' in x):
        return False
    return True
    
def checkVowels(x):
    count = 0
    for _ in x:
        if (_ == 'a' or _ == 'e' or _ == 'i' or _ == 'o' or _ == 'u'):
            count += 1
    return count >= 3

def checkNoDoubles(string):
    for i in range(len(string) - 1):
        if (string[i] == string[i + 1]):
            return True
    return False

    
def checkNice(string):
    return checkVowels(string) and checkNoPairs(string) and checkNoDoubles(string)

def countNice(data):
    count = 0
    for _ in data:
        if checkNice(_):
            count += 1
    print(count)

    
# countNice(data)

# part two

def checkNonOverlappingDoubles(string):
    for i in range(len(string) - 2):
        if (string[i:i+2] in string[i+2:]):
            return True
    return False

def checkNextDoorButOneNeighbours(string):
    for i in range(len(string) - 2):
        if (string[i] == string[i+2]):
            return True
    return False

def checkNewCount(data):
    count = 0
    for _ in data:
        if checkNonOverlappingDoubles(_) and checkNextDoorButOneNeighbours(_):
            count += 1
    print(count)



checkNewCount(data)





# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?