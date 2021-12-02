n = 0 # the amount of sums that are larger than the previous one

with open('./input.txt', 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if i and line:
            if int(line) > int(previous):
                n+=1
        previous = line
    f.close()
    
print(n)