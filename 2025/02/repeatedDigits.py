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


def formatRange(code):
    range = code.split('-')
    number = int(range[0])
    end = int(range[1])
    total = 0
    while number < end:
        number += 1
        if isRepeatedDigit(number):
            total += number
        if hasRepeatedDigits(number):
            total += number
    return total


def main(code):
    IDtotal = 0
    for range in code:
        total = formatRange(range)
        IDtotal += total
    return IDtotal


print(main(IDs))