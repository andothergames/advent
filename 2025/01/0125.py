# safe combination


with open('0125input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

def spinDial(dir, amt, start):
    position = start
    for x in range(amt):
        if dir == 'R':
            position += 1
            if position == 100:
                position = 0
        if dir == 'L':
            position -= 1
            if position == -100:
                position = 0
    return position


def formatData(data):
    directions = []
    for string in data:
        dir = string[0]
        amt = int(string[1:])
        directions.append([dir, amt])
    return directions

        

def main(data):
    dirs = formatData(data)
    zeroesCount = 0
    startPosition = 50
    for line in dirs:
        position = spinDial(line[0], line[1], startPosition)
        if position == 0:
            zeroesCount += 1
        startPosition = position
    return zeroesCount
    

print(main(data))