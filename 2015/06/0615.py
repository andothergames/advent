# --- Day 6: Probably a Fire Hazard ---


with open('0615input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

lights = {}


def getCoords(line):
    splitLine = line.split(' ')

    if splitLine[1] == 'off':
        nums = splitLine[2] + ',' + splitLine[4]
        return formatCoords(nums, 'off')
    
    if splitLine[1] == 'on':
        nums = splitLine[2] + ',' + splitLine[4]
        return formatCoords(nums, 'on')
    
    if splitLine[0] == 'toggle':
        nums = splitLine[1] + ',' + splitLine[3]
        return formatCoords(nums, 'toggle')


def formatCoords(n, command):
    instruction = [int(i) for i in n.split(",")]
    instruction.insert(0, command)
    return instruction

#toggle toggle 720,196 through 897,994

def operateLights(i):

    if i[0] == 'on':
        turnLight(i[1], i[2], i[3], i[4], True)
    if i[0] == 'off':
        turnLight(i[1], i[2], i[3], i[4], False)
    if i[0] == 'toggle':
        toggleLight(i[1], i[2], i[3], i[4])
    

def turnLight(a, b, c, d, value):
    xRange = c - a 
    yRange = d - b 
    x = a 
    y = b 
    for _ in range(yRange + 1):
        x = a
        for _ in range(xRange + 1):
            key = f'{x},{y}'
            lights[key] = value
            x += 1
        y += 1   


def toggleLight(a, b, c, d):
    xRange = c - a 
    yRange = d - b 
    x = a 
    y = b 
    for _ in range(yRange + 1):
        x = a
        for _ in range(xRange + 1):
            key = f'{x},{y}'
            if key in lights.keys():
                lights[key] = not lights[key]
            else:
                lights[key] = True
            x += 1
        y += 1 



def countLights(data):
    for line in data:
        instruction = getCoords(line)
        operateLights(instruction)
    

countLights(data)
count = len([v for v in lights.values() if v is True])

print(count)
