import numpy
def check_win(boards):
    test = numpy.ones((len(boards), 5, 5))
    for value in randoms.split(','):
        for i in range(len(test)):
            test[i][boards[i] == int(value)] = 0
            #print(numpy.where(~test[i].any(axis=1))[0])
            if len(numpy.where(~test[i].any(axis=1))[0]) == 1 or len(numpy.where(~test[i].any(axis=0))[0]) == 1: # checks if everything is zero
                return i, value, test[i] 
        #print(test)

def calculate_the_sum(boards):
    new_sum = 0
    index, board_number, test_board = check_win(boards)
    #print(boards[index], '\n\n', test_board)
    for line_index in range(len(boards[index])):
        for i in range(len(boards[index][line_index])):
            #print(test_board[line_index, i], '\n\n\n')
            #print(test_board[line_index, i] == True, '|', boards[index][line_index][i])
            if test_board[line_index, i]:
                new_sum += boards[index][line_index][i]
    return int(board_number), new_sum

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




    
    