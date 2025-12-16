import re

with open('1615input.txt', 'r') as file:
    text = file.readlines()

aunts = {}

MFCSAM = {
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

compounds = MFCSAM.keys()

#  1: {'comp': num, 'comp': num}

def checkCompounds(data):
    for _ in MFCSAM:
        for compound in data:
            if data[compound] != MFCSAM[_]:
                return False
        print(data)
        return True 


def formatData(data):
    for line in data:
        text = line.rstrip()
        auntData = re.split(r'[:,\s]+', text)
        compounds = {}

        compounds[auntData[2]] = int(auntData[3])
        compounds[auntData[4]] = int(auntData[5])
        compounds[auntData[6]] = int(auntData[7])

        aunts[int(auntData[1])] = compounds
        compounds = {}
    print(aunts)

# formatData(text)

def searchAunts(): 
    key = 1
    while key < 500:
        for compound in aunts[key]:
            if compound in compounds:
                checkCompounds(aunts[key])

        key += 1
