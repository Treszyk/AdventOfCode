total_amount = 0

with open('./input.txt') as f:
    dimensions = [line.strip().split('x') for line in f]
    
for values in dimensions:
    l, w , h = [int(value) for value in values]
    s1 = l * w
    s2 = w * h
    s3 = h * l 
    paper_amount = 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)
    total_amount += paper_amount

print(f'Amount of paper needed for wrapping: {total_amount}')