def get_string_diff(str1, str2):
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    return str2.replace(str1, '')

def compare_string(strings, str2):
    for one_str in strings:
        for letter in one_str:
            if letter not in str2:
                return False
    return True


with open('./input.txt', 'r') as f:
    data = f.read().split('\n')

my_sum = 0
for line in data:# i'm sorry for this if, elif abomination I just couldn't figure a better way to do it. I was desperate to just make it work
    values, output = line.split(' | ')
    values = [digit for digit in values.split()]
    output = [code for code in output.split()]
    known_digits = {}
    for coded_digit in reversed(values):
        if(len(coded_digit) == 2):
            known_digits[1] = coded_digit
            del values[values.index(coded_digit)]
        if(len(coded_digit) == 4):
            known_digits[4] = coded_digit
            del values[values.index(coded_digit)]
        if(len(coded_digit) == 3):
            known_digits[7] = coded_digit
            del values[values.index(coded_digit)]
        if(len(coded_digit) == 7):
            known_digits[8] = coded_digit
            del values[values.index(coded_digit)]

    while len(values):
        for coded_digit in reversed(values):
            if len(coded_digit) == 5:
                if compare_string([known_digits[1]], coded_digit):
                    known_digits[3] = coded_digit
                    del values[values.index(coded_digit)]
                elif known_digits.get(9) and not known_digits.get(5):
                    if compare_string([coded_digit], known_digits[9]):
                        known_digits[5] = coded_digit
                        del values[values.index(coded_digit)]
                elif known_digits.get(5):
                    known_digits[2] = coded_digit
                    del values[values.index(coded_digit)]
            elif len(coded_digit) == 6 and known_digits.get(3):
                if compare_string([known_digits[3]], coded_digit):
                    known_digits[9] = coded_digit
                    del values[values.index(coded_digit)]
                elif known_digits.get(5):
                    if compare_string([known_digits[5]], coded_digit):
                        known_digits[6] = coded_digit
                        del values[values.index(coded_digit)]
                    elif known_digits.get(6):
                        known_digits[0] = coded_digit
                        del values[values.index(coded_digit)]

    known_digits = {''.join(sorted(key)): val for val, key in known_digits.items()}
    code = ''
    for i in output:
        code += str(known_digits[''.join(sorted(i))])
    print(code)
    my_sum += int(code)
print(f'A total sum of the output values is {my_sum}')
