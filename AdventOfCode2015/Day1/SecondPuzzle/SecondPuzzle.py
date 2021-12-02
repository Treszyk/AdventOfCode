floor = 0
pos = 1
with open('./input.txt', 'r') as f:
    instr = f.read()
    for char in instr:
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(f'Santa entered the basement at position: {pos}')
            break
        pos += 1