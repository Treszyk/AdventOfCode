n = 0 # the amount of sums that are larger than the previous one
values = [] # holds the sums

with open('./input.txt', 'r') as file:
    inputs = [int(line.strip()) for line in file]
    for i in range(len(inputs)):
        newSum = sum(inputs[i:i+3])
        values.append(newSum)
    file.close()  
    for i in range(1, len(values)):
        n = n + 1 if values[i - 1] < values[i] else n 
print(n)