# // --- Day 2: I Was Told There Would Be No Math ---
# https://adventofcode.com/2015/day/2


data = []
with open('0212input.txt') as inputfile:
    for line in inputfile:
        dimensions = sorted(map(int, line.split('x')))
        data.append(dimensions)

def calcArea(x,y):
    return x * y


def calcSingleWrapping(dims):
    area1 = calcArea(dims[0], dims[1])
    area2 = calcArea(dims[1], dims[2])
    area3 = calcArea(dims[0], dims[2])
    return ((area1 + area2 + area3) * 2) + area1


def calcTotalWrapping(presents):
    total = 0
    for dims in presents:
        t = calcSingleWrapping(dims)
        total += t
    return total

def calcRibbon(presents):
    total = 0
    for dims in presents:
        sides = dims[0]*2 + dims[1]*2
        bow = dims[0] * dims[1] * dims[2]
        ribbon = sides + bow
        total += ribbon
    return total
    
print(calcTotalWrapping(data))
print(calcRibbon(data))