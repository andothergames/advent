with open('0716input.txt', 'r') as file:
    codes = [line.strip() for line in file.readlines()]

import re


def formatCode(code):
    return re.split(r'[\[\]\s]+', code)


def isABBA(s):
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def checkCode(string):
    i = 0 
    while i < len(string) - 3:
        if isABBA(string[i:i+4]):
            return True
        i += 1
    return False


def isTLS(codes):
    i = 0
    checker = False
    while i < len(codes):
        if i % 2 != 0:
            if checkCode(codes[i]):
                return False
        if i % 2 == 0:
            if checkCode(codes[i]):
                checker = True
        i += 1
    return checker


def main(codes):
    TLS = 0
    for line in codes:
        list = formatCode(line)
        if isTLS(list):
            TLS += 1
    return TLS


print(main(codes))