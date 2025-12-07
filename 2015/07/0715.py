# --- Day 7: Some Assembly Required ---

with open('0715input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

# this is where the solved circuits will go
codes = {}
# this is where the split instructions formatted with  circuit letter(s) first then x amt of other things in an array (the instruction)
circuits = {}
# circuits that havent been solved yet
wip = ['a']


#straightforward in data
# lx -> a
# 1674 -> b
# 0 -> c

def main(x):
    formatCodes(x)
    scrubCircuits(circuits)
    print(codes)
    for _ in range(339):
        tester = wip[-1]
        hunt(tester)
    print(circuits)

#big beefy
def hunt(x):
    # if x in codes:
    #     print(x, 'fish fish i found a fish')
    if 'NOT' in circuits[x]:
        wip.append(circuits[x][1])
    if 'AND' in circuits[x] or 'OR' in circuits[x]:
        if not circuits[x][0].isnumeric():
            wip.append(circuits[x][0])
        if not circuits[x][2].isnumeric():
            wip.append(circuits[x][2])
    if 'LSHIFT' in circuits[x] or 'RSHIFT' in circuits[x]:
        wip.append(circuits[x][0])


def formatCodes(data):
    for line in data:
        splitLine = line.split(' -> ')
        key = splitLine[1]
        if checkOperators(splitLine[0]):
            value = splitLine[0].split(' ')
        else:
            value = splitLine[0]
        circuits[key] = value

# this goes through initial list and saves out nice and neat circuits that have integers assigned to the codes list
def scrubCircuits(circuits):
    for _ in circuits:
        if type(circuits[_]) != list:
            if circuits[_].isnumeric():
                value = int(circuits[_])
                codes[_] = value
            else:
                wip.append(circuits[_])


def checkOperators(s):
    operators = ['NOT', 'OR', 'AND', 'LSHIFT', 'RSHIFT']
    for _ in operators:
        if _ in s:
            return True
    return False




main(data)