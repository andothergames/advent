import re

with open('1615input.txt', 'r') as file:
    data = file.readlines()

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


def checkCompounds(compound, aunt):
    if compound == 'trees' or compound == 'cats':
        return aunt[compound] > MFCSAM[compound]
    if compound == 'pomeranians' or compound == 'goldfish':
        return aunt[compound] < MFCSAM[compound]
    else:
        return aunt[compound] == MFCSAM[compound]


# aunts value is more than the ticker cats and trees 
# aunts value is less than pomeranians and goldfish 

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
    return aunts


def searchAunts(a): 
    for key, compounds in a.items():
        if all(checkCompounds(compound, compounds) for compound in compounds):
            print(f"Aunt {key}")
            return True
    return False


sues = formatData(data)
searchAunts(sues)