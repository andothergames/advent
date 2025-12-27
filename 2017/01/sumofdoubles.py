with open('0117input.txt', 'r') as inputfile:
    numbers = list(inputfile.read())

total = 0
i = 0

while i < len(numbers) - 1:
    if numbers[i] == numbers[i + 1]:
        total += int(numbers[i])
    i += 1

if numbers[0] == numbers[-1]:
    total += int(numbers[0])

print(total)