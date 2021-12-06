with open('./input.txt', 'r') as f:
    list_of_fish = [int(fish) for fish in f.read().split(',')]

for day in range(80):
    new_fish = []
    for i in range(len(list_of_fish)):
        list_of_fish[i] -= 1
        if list_of_fish[i] < 0:
            list_of_fish[i] = 6
            new_fish.append(8)
    list_of_fish += new_fish
    
print(f'The amount of fish on the 80th day is: {len(list_of_fish)}')