def bin_to_decimal(binInAList):
    power = 0
    decimal = 0

    for bit in reversed(binInAList):
        decimal += (2**power) * int(bit)
        power += 1

    return decimal


most_common = []
least_common = []

with open('./input.txt') as f:
    lis = [code.strip() for code in f]

for column in range(len(lis[0])):
    value = 0

    for row in lis: #
        if(row[column] == '1'):
            value += 1
        else:
            value -= 1

    if value > 0:
        most_common.append('1')
        least_common.append('0')
    else:
        most_common.append('0')
        least_common.append('1')

gamma_rate = bin_to_decimal(most_common)
epsilon_rate = bin_to_decimal(least_common)
print(f'The power consumption is: {gamma_rate * epsilon_rate}')
