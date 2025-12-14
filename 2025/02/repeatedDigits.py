with open('0225input.txt', 'r') as file:
    IDs = file.read().split(',')


def hasRepeatedDigits(digit):
    checker  = False
    number = str(digit)
    midpoint = int(len(number) / 2)
    if number[0:midpoint] == number[midpoint:]:
        checker = True 
    return checker


def isRepeatedDigit(n):
    checker = True
    number = str(n)
    digit = 0
    while digit < 10:
        if digit != number[0]:
            checker = False
        digit += 1
    return checker


def formatRange(code, method):
    range = code.split('-')
    number = int(range[0])
    end = int(range[1])
    total = 0
    if method == 1:
        while number < end:
            number += 1
            if isRepeatedDigit(number):
                total += number
            if hasRepeatedDigits(number):
                total += number
    if method == 2:
        while number < end:
            number += 1
            if isRepeatedDigit(number):
                total += number

    return total


def findFactors(x):
    factors = []
    for i in range(1, x):
       if x % i == 0:
           factors.append(i)
    factors.pop(0)
    return factors


def repeatedDigits(n):
    strNum = str(n)
    number = len(strNum)
    factors = findFactors(number)
    match = False
    
    for x in factors:
        start = 0
        end = x
        y = 0
        segment = strNum[start:end]
        if match == True:
            return match
        while y < len(strNum):
            print(strNum[start:end])
            if strNum[start:end] == segment:
                match = True
            else:
                match = False
            end += x
            start += x
            y += x

    return match



def main(code, method):
    IDtotal = 0
    if method == 1:
        for range in code:
            total = formatRange(range)
            IDtotal += total
    if method == 2:
        for range in code:
            total = repeatedDigits(range)
            IDtotal += total
    return IDtotal


# print(main(IDs))