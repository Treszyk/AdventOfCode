import numpy

with open('input.txt', 'r') as f:
    list_of_points = f.read()

grid = numpy.zeros([1000, 1000])

list_of_points = list_of_points.split('\n')
for i, points in enumerate(list_of_points): # this loop turns the list_of_points into a list of dictionaries of points like: [{'x1': 5, 'y1': 4, 'x2': 3, 'y2': 4}, ]
    list_of_points[i] = points.replace(' -> ', ' ')
    list_of_points[i] = list_of_points[i].split()
    dict_of_points = {}
    
    for j, point in enumerate(list_of_points[i]):
        x = point.split(',')[0]
        y = point.split(',')[1]
        dict_of_points[f'x{j+1}'] = int(x)
        dict_of_points[f'y{j+1}'] = int(y)
    list_of_points[i] = dict_of_points

for points in list_of_points:
    x1 = points['x1']
    x2 = points['x2']

    y1 = points['y1']
    y2 = points['y2']

    if points['x1'] == points['x2']:
        for new_y in range(min(y1,y2), max(y1, y2) + 1): # this loop iterates over all the y values between the points
            grid[new_y][x1] += 1
    elif points['y1'] == points['y2']:
        for new_x in range(min(x1,x2), max(x1, x2) + 1): # this loop iterates over all the x values between the points
            grid[y1][new_x] += 1

print(f'Two lines overlap in at least: {len(grid[grid >= 2])} lines')
