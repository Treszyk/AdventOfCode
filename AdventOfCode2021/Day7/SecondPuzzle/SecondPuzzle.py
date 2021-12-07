from collections import defaultdict

values = defaultdict(int)
with open('./input.txt', 'r') as f:
    for value in f.read().strip().split(','):
        value = int(value)
        values.setdefault(value, 0)
        values[value] += 1

fuel = 0
for pos in range(max(values.keys()) + 1): # this checks every possible position
    new_fuel = 0
    for key, n in values.items():
        new_fuel += ((1 + abs(key - pos))/2) * abs(key - pos) * n # here we add a sum of sequence 1, 2, 3... it represents the change in the amount of burned fuel
    if not fuel:
        fuel = new_fuel
    elif new_fuel < fuel:
        fuel = new_fuel
print(f'They must spend: {int(fuel)} fuel')
