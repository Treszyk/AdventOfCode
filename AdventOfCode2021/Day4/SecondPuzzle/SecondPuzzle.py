import numpy
def check_lost(boards):
    test_array = numpy.ones((len(boards), 5, 5))
    winning = numpy.zeros((len(boards)), dtype=bool)
    num_of_winning_boards = 0
    for value in randoms.split(','):
        for i in range(len(test_array)):
            test_array[i][boards[i] == int(value)] = 0
            #print(numpy.where(~test_array[i].any(axis=1))[0])
            if (len(numpy.where(~test_array[i].any(axis=1))[0]) == 1 or len(numpy.where(~test_array[i].any(axis=0))[0]) == 1) and winning[i] == False: # checks if everything is zero
                winning[i] = True
                num_of_winning_boards+=1
                if len(boards) - num_of_winning_boards == 0:
                    return i, value, test_array[i]

        #print(test_array)

def calculate_the_sum(boards):
    new_sum = 0
    index, last_value, test_array_board = check_lost(boards)
    #print(boards[index], '\n\n', test_array_board)
    for line_index in range(len(boards[index])):
        for i in range(len(boards[index][line_index])):
            #print(test_array_board[line_index, i], '\n\n\n')
            #print(test_array_board[line_index, i] == True, '|', boards[index][line_index][i])
            if test_array_board[line_index, i]:
                new_sum += boards[index][line_index][i]
    return int(last_value), new_sum

def turn_boards_into_arrays(boards):
    boards_array = []
    boardLines = [line.split('\n') for line in boards]

    for block in boardLines:
        block = [values.split() for values in block]
        boards_array.append(block)

    return boards_array
with open('./input.txt') as f:
    inp = f.read().split('\n\n')
    randoms = inp[0].strip()
    boards = inp[1:]
    
#for i in boards:
#    for j in i:
#        new_boards.append([[value] for value in j.split()])

boards = turn_boards_into_arrays(boards)  
boards = numpy.array(boards)
boards = boards.astype(numpy.int64)
board_num, unchecked_sum = calculate_the_sum(boards)
print(f'The final score will be: {board_num * unchecked_sum}')




    
    