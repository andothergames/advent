with open('0616input.txt', 'r') as file:
    codes = [line.strip() for line in file.readlines()]

testCodes = ['mjgvdqpx', 'lrxbguep', 'mtxiguep', 'wvxifimw', 'mrxvmwye']

letterCount = {0: {},
               1: {},
               2: {},
               3: {},
               4: {},
               5: {},
               6: {},
               7: {}}

for line in codes:
    char = 0
    while char < len(line):
        letter = line[char]
        letterCount[char][letter] = letterCount[char].get(letter, 0) + 1
        char += 1

for count in letterCount:
    print(max(letterCount[count], key=letterCount[count].get))
