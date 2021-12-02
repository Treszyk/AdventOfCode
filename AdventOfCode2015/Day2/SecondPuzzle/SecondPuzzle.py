total_paper_amount = 0
total_ribbon_amount = 0

with open('./input.txt') as f:
    dimensions = [line.strip().split('x') for line in f]
    
for values in dimensions:
    l, w , h = [int(value) for value in values]
    s1 = l * w
    s2 = w * h
    s3 = h * l 

    paper_amount = 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)
    total_paper_amount += paper_amount

    ribbon_amount = min(l+l+w+w, l+l+h+h, w+w+h+h)
    bow_amount = l * w * h
    total_ribbon_amount += ribbon_amount + bow_amount

print(f'Amount of paper needed for wrapping: {total_paper_amount}\n',
      f'Amount of ribbon needed for wrapping: {total_ribbon_amount}', sep='')