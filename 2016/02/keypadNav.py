with open('0216input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

def compute(n, i):
    if i == "R":
        if n != 3 and n != 6 and n != 9:
            return n + 1
        if n == 3 or n == 6 or n == 9:
            return n
    if i == "L":
        if n != 1 and n != 4 and n != 7:
            return n - 1
        if n == 1 or n == 4 or n == 7:
            return n
    if i == "U":
        if n != 1 and n != 2 and n != 3:
            return n - 3
        if n == 1 or n == 2 or n == 3:
            return n
    if i == "D":
        if n != 7 and n != 8 and n != 9:
            return n + 3
        if n == 7 or n == 8 or n == 9:
            return n
        




def compute2(n, i):
    col1 = ['2', '6']
    col2 = ['3', '7']
    col3 = ['4', '8']

    row1 = ['2', '3', '4']
    row2 = ['6', '7', '8']

    if i == 'R':
        if n == '5':
            return '6'
        if n == 'A':
            return 'B'
        if n == 'B':
            return 'C'
        if n in col1 or n in col2 or n == "8":
            return str(int(n) + 1)
        else:
            return n
        
    if i == 'L':
        if n == '9':
            return '8'
        if n == 'B':
            return 'A'
        if n == 'C':
            return 'B'
        if n in col2 or n in col3 or n == '6':
            return str(int(n) - 1)
        else:
            return n
    
    if i == 'U':
        if n == 'D':
            return 'B'
        if n == 'A':
            return '6'
        if n == 'B':
            return '7'
        if n == 'C':
            return '8'
        if n == 'D':
            return 'B'
        if n == "3":
            return "1"
        if n in row2:
            return str(int(n) - 4)
        else: 
            return n
        
    if i == 'D':
        if n == '1':
            return '3'
        if n == '6':
            return 'A'
        if n == '7':
            return 'B'
        if n == '8':
            return 'C'
        if n == 'B':
            return 'D'
        if n in row1:
            return str(int(n) + 4)
        else:
            return n
        

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

def main(data):
    password = []
    n = '5'
    for line in data:
        instruction = list(line)
        for i in instruction:
            n = compute2(n, i)
        password.append(n)
    return "".join(password)
        

print(main(data))
