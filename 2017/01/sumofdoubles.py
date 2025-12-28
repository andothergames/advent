with open('0117input.txt', 'r') as inputfile:
    numbers = list(inputfile.read())

total1 = 0
i = 0

while i < len(numbers) - 1:
    if numbers[i] == numbers[i + 1]:
        total1 += int(numbers[i])
    i += 1

if numbers[0] == numbers[-1]:
    total1 += int(numbers[0])

# print('1.1', total)

total1 = 0
length = len(numbers)
halfway = length // 2

for j in range(length):
    if numbers[j] == numbers[(j + halfway) % length]:
        total1 += int(numbers[j])

# print(total1)