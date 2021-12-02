with open('./input.txt', 'r') as f:
    instr = f.read()

print(f"The instr took Santa to the floor number: {instr.count('(') - instr.count(')')}")
