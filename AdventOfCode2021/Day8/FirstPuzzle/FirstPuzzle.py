with open('./input.txt', 'r') as f:
    data = f.read().split('\n')
    values = [line.split(' | ')[0] for line in data]
    output = [line.split(' | ')[1] for line in data]

how_many = 0

for digits in output:
    for digit in digits.split():
        match len(digit):
            case 2:
                how_many += 1
            case 3:
                how_many += 1
            case 4:
                how_many += 1
            case 7:
                how_many += 1
            case _:
                pass

print(how_many)

