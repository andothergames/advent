# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

with open('0315input.txt', 'r') as inputfile:
    directions = list(inputfile.read())

houses = {'0,0': 1}
roboHouses = {'0,0': 2}

def logHouses(dirs):
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

def logHousesWithRobo(dirs):
    counter = 0
    santax = 0
    santay = 0
    robox = 0
    roboy = 0

    for _ in dirs:
        counter += 1
        if counter % 2 == 1:
            #santa goes
            if _ == '^':
                santax += 1
            if _ == 'v':
                santax -= 1
            if _ == '>':
                santay += 1
            if _ == '<':
                santay -= 1
            key = f'{santax},{santay}'
            roboHouses[key] = roboHouses.get(key, 0) + 1

        if counter % 2 == 0:
            #robo goes
            if _ == '^':
                robox += 1
            if _ == 'v':
                robox -= 1
            if _ == '>':
                roboy += 1
            if _ == '<':
                roboy -= 1
            key = f'{robox},{roboy}'
            roboHouses[key] = roboHouses.get(key, 0) + 1
    print(len(roboHouses))

logHouses(directions)
logHousesWithRobo(directions)
