with open('0325input.txt', 'r') as file:
    batteries = file.readlines()
    

def findFirstHighestNumber(x):
    y = 9
    while y > 0:
        if str(y) in x[0:-1]:
            return y
        y -= 1


def findSecondHighestNumber(x):
    y = 9
    while y > 0:
        if str(y) in x:
            return y
        y -= 1


def main(code):
    totalJoltage = 0
    for line in code:
        first = findFirstHighestNumber(line.strip())
        position = line.index(str(first))
        second = findSecondHighestNumber(line[position + 1:])
        highest = str(first) + str(second)
        totalJoltage += int(highest)
    print(totalJoltage)


main(batteries)