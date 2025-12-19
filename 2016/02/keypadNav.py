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
        
def main(data):
    password = []
    n = 5
    for line in data:
        instruction = list(line)
        for i in instruction:
            n = compute(n, i)
        password.append(str(n))
    return "".join(password)
        
print(main(data))