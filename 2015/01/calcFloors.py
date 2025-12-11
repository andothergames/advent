# https://adventofcode.com/2015/day/1


with open('0115input.txt', 'r') as inputfile:
    directions = list(inputfile.read())

def calcFloor(dirs):
    floor = 0
    for _ in dirs:
        if _ == '(':
            floor += 1
        if _ == ')':
            floor -= 1
    return floor


def basementWhen(dirs):
    floor = 0
    counter = 0
    for _ in dirs:
        counter += 1
        if _ == '(':
            floor += 1
        if _ == ')':
            floor -= 1
        if floor < 0:
            break
    return counter


print(calcFloor(directions))
print(basementWhen(directions))