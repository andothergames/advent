with open('0116input.txt', 'r') as inputfile:
    directions = inputfile.read().split(', ')
    

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


def calcDirs(directions):
    coords = [0, 0, 'N']
    for dir in directions:
        coords[2] = changeDir(coords[2], dir[0])
        dist = int(dir[1:])

        if coords[2] == 'N':
            coords[1] = coords[1] + dist
        if coords[2] == 'E':
            coords[0] = coords[0] + dist
        if coords[2] == 'S':
            coords[1] = coords[1] - dist
        if coords[2] == 'W':
            coords[0] = coords[0] - dist

    print(coords)


calcDirs(directions)
