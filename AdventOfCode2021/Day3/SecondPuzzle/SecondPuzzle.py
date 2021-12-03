def bin_to_decimal(binInAList):
    """
    Takes a list with bits in seperate indexes and calculates its decimal value
    """
    power = 0
    decimal = 0

    for bit in reversed(binInAList):
        decimal += (2**power) * int(bit)
        power += 1

    return decimal

def get_gamma_and_epsilon_rate(inputList):
    """
    Takes an inputList and returns gamma and epsilon rates
    """
    gamma_rate = []
    epsilon_rate = []
    for column in range(len(inputList[0])):
        value = 0

        for row in inputList: #
            if(row[column] == '1'):
                value += 1
            else:
                value -= 1

        if value > 0:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            gamma_rate.append('0')
            epsilon_rate.append('1')

    return bin_to_decimal(gamma_rate), bin_to_decimal(epsilon_rate)

def get_o2_or_co2_rating(inputList, co2=False):
    """
    Takes an inputList and depending on the param 'co2' returns the o2 rating if it's False and returns co2 when it's true
    """
    for column in range(len(inputList[0])):
        value = 0
        rows1 = []
        rows0 = []

        for row in inputList: #
            if(row[column] == '1'):
                value += 1
                rows1.append(row)
            else:
                rows0.append(row)
                value -= 1

        if len(inputList) == 1:
            break
        if value > 0:
            inputList = rows0 if co2 else rows1
        elif value == 0:
            inputList = rows0 if co2 else rows1
        else:
            inputList = rows1 if co2 else rows0

    return bin_to_decimal([bit for bit in inputList[0]])


with open('./input.txt') as f:
    lis = [code.strip() for code in f]

gamma_rate, epsilon_rate = get_gamma_and_epsilon_rate(lis) 
o2_generator_rating = get_o2_or_co2_rating(lis)
co2_scrubber_rating = get_o2_or_co2_rating(lis, co2=True)

print(f'The power consumption is: {gamma_rate * epsilon_rate}')
print(f'The life support rating is: {o2_generator_rating * co2_scrubber_rating}')