from collections import defaultdict

fish = defaultdict(int) # defaultdict is a dictionary that wont cause a keyerror when you try to access an unassigned key

with open('./input.txt', 'r') as f:
    list_of_fish = [int(fish) for fish in f.read().split(',')]

for i in list_of_fish: # if a value from input doesnt exist in the dictionary we set it to zero
    fish.setdefault(i, 0)
    fish[i] += 1

for day in range(256):
    fish_after = defaultdict(int) # this will be our dictionary after one day
    for key, value in fish.items(): 
        if key == 0: # key represents the type of fish we have and the value means how many of them we have for example if key = 0 and value = 3 that means there are 3 fish with 0 days left
            fish_after[6] += value
            fish_after[8] += value
        else:
            fish_after[key-1] += value
    fish = fish_after # we update our main dictionary with the values after one day
    #print(dict(fish))
print(sum(fish.values()))
