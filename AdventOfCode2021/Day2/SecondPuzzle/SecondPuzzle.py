horizontal_pos = 0
depth = 0
aim = 0

with open('./input.txt', 'r') as file:
    for line in file:
        key = line.strip().split()[0]
        value = int(line.strip().split()[1])
        
        if key == 'forward':
            horizontal_pos += value
            depth += abs(aim * value)
        elif key == 'up':
            aim -= value
        else:
            aim += value

print(f'The result is: {horizontal_pos * depth}')