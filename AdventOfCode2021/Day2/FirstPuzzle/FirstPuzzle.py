horizontal_pos = 0
depth = 0

with open('./input.txt', 'r') as f:
    for line in f:
        key = line.strip().split()[0]
        value = int(line.strip().split()[1])
        if key == 'forward':
            horizontal_pos += value
        elif key == 'up':
            depth += value
        else:
            depth -= value
    f.close()

print(f'The result is: {abs(horizontal_pos * depth)}')