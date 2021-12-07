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
        amount_of_fuel = abs(key-pos)
        new_fuel += amount_of_fuel * n
    if not fuel:
        fuel = new_fuel
    elif new_fuel < fuel:
        fuel = new_fuel
print(f'They must spend: {int(fuel)} fuel')