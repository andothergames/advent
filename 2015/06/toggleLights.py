# --- Day 6: Probably a Fire Hazard ---


with open('0615input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

lights = {}
lights2 = {}

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
    

# countLights(data)
count = len([v for v in lights.values() if v is True])
# print(count)




def lightShowRoundTwo(data):
    for line in data:
        instruction = getCoords(line)
        brightenLights(instruction, )

def brightenLights(i):

    xRange = i[3] - i[1]
    yRange = i[4] - i[2] 
    x = i[1]
    y = i[2]

    for _ in range(yRange + 1):
        x = i[1]
        for _ in range(xRange + 1):
            key = f'{x},{y}'
            if i[0] == 'on':
                lights2[key] = lights2.get(key, 0) + 1
            if i[0] == 'off':
                if key in lights2:
                    if lights2[key] > 0:
                        lights2[key] = lights2.get(key, 0) - 1

            if i[0] == 'toggle':
                lights2[key] = lights2.get(key, 0) + 2
            x += 1
        y += 1  


lightShowRoundTwo(data)
print(sum(lights2.values()))
