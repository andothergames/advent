# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

with open('0315input.txt', 'r') as inputfile:
    directions = list(inputfile.read())

houses = {'0,0': 1}

def logHouse(dirs):
    x = 0
    y = 0
    for _ in dirs:
        if _ == '^':
            x += 1
        if _ == 'v':
            x -= 1
        if _ == '>':
            y += 1
        if _ == '<':
            y -= 1
        key = f'{x},{y}'
        houses[key] = houses.get(key, 0) + 1
    print(len(houses))

logHouse(['^','>','v','<', '^'])
