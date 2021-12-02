horizontal_pos = 0
depth = 0

with open('./input.txt', 'r') as file:
    for line in file:
        key = line.strip().split()[0]
        value = int(line.strip().split()[1])
        if key == 'forward':
            horizontal_pos += value
        elif key == 'up':
            depth += value
        else:
            depth -= value

print(f'The result is: {abs(horizontal_pos * depth)}')