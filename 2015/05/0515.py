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

    
countNice(data)
