with open('0116input.txt', 'r') as inputfile:
    directions = inputfile.read().split(', ')
    
locations = {}

def changeDir(current, turn):
    if current == 'N' and turn == 'R':
        return 'E'
    if current == 'N' and turn == 'L':
        return 'W'
    if current == 'E' and turn == 'R':
        return 'S'
    if current == 'E' and turn == 'L':
        return 'N'
    if current == 'S' and turn == 'R':
        return 'W'
    if current == 'S' and turn == 'L':
        return 'E'
    if current == 'W' and turn == 'R':
        return 'N'
    if current == 'W' and turn == 'L':
        return 'S'


def moveDistance(C, dist):
    for _ in range(dist):
        if C[2] == 'N':
            C[1] += 1
            key = f"{C[0]},{C[1]}"
            if key in locations.keys():
                print(key, 'key')
                break
            else:
                locations[key] = 1
        if C[2] == 'E':
            C[0] += 1
            key = f"{C[0]},{C[1]}"
            if key in locations.keys():
                print(key, 'key')
                break
            else:
                locations[key] = 1
        if C[2] == 'S':
            C[1] -= 1
            key = f"{C[0]},{C[1]}"
            if key in locations.keys():
                print(key, 'key')
                break
            else:
                locations[key] = 1
        if C[2] == 'W':
            C[0] -= 1
            key = f"{C[0]},{C[1]}"
            if key in locations.keys():
                print(key, 'key')
                break
            else:
                locations[key] = 1
    return C

        

def calcDirs(directions):
    coords = [0, 0, 'N']
    for dir in directions:
        coords[2] = changeDir(coords[2], dir[0])
        dist = int(dir[1:])
        newCoords = moveDistance(coords, dist)
        coords = newCoords
    print(coords)


calcDirs(directions)