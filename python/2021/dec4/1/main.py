import re
boards = {}
numbers = []
with open('2021/dec4/input.txt', 'r') as inputfile:
    tableindex = -1
    for line in inputfile:
        line = line.strip()
        if ',' in line:
            numbers = line.split(',')
        else:
            if len(line) == 0:
                tableindex += 1
                boards[tableindex] = []
            else:
                newline = re.split(' +', line)
                
                # print(newline)
                boards[tableindex].append(newline)

def print_board(myboard):
    for row in myboard:
        for column in row:
            print(f"{column:3} ", end='')
        print()
    print()

def print_boards(myboards):
    for board in myboards.values():
        print_board(board)

def calculate_board(myboard):
    sum = 0
    for row in myboard:
        for col in row:
            if col != 'X':
                sum += int(col)

    return sum


winner_board = None
winner_boardid = None
winner_number = None
bingo = False
winlist = []
for number in numbers:
    for boardid, board in boards.items():
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == number:
                    board[row][col] = "X"
    # check if we hve bingo
    for boardid, board in boards.items():
        for row in board:
            if ''.join(row) == 'XXXXX':
                print("bingo!")
                bingo = True
                winner_board = board
                winner_number = number
                winner_boardid = boardid
            columns = {}
        for col in range(len(board)):
            for row in range(len(board)):
                columns[col] = [x for x in board[row][col]]
            if ''.join(columns[col]) == 'XXXXX':
                print("bingo!")
                bingo = True
                winner_board = board
                winner_boardid = boardid
                winner_number = number

    if bingo:
        break
print_boards(boards)
print(f"the winner board is {winner_boardid} out of {len(boards.keys())}")
print_board(winner_board)
print_board(boards[winner_boardid])
print(int(winner_number))
print(calculate_board(winner_board))
print( calculate_board(winner_board) * int(winner_number))