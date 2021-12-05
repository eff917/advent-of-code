import re
from copy import deepcopy
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

original = deepcopy(boards)
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

number_of_boards = len(boards.keys())

winner_board = None
winner_boardid = None
winner_number = None
bingo = False
winlist = set()
for number in numbers:
    for boardid, board in boards.items():
        if boardid not in winlist:
            for row in range(len(board)):
                for col in range(len(board)):
                    if board[row][col] == number:
                        board[row][col] = "X"
    # check if we hve bingo
    for boardid, board in boards.items():
        # check rows
        if boardid not in winlist:
            for row in board:
                if ''.join(row) == 'XXXXX':
                    print(f"bingo! number: {number} boardid: {boardid} row:{row} winner boards count: {len(winlist)}")
                    print( calculate_board(board * int(number)))
                    bingo = True
                    winner_board = board
                    winner_number = number
                    winner_boardid = boardid
                    if len(boards.keys()) > len(winlist):
                        winlist.add(boardid)
                        bingo = False
                # check columns
            columns = {}
            for col in range(len(board)):
                columns[col] = []
                for row in range(len(board)):
                    columns[col].append(board[row][col].strip())
                if ''.join(columns[col]) == 'XXXXX':
                    print(f"bingo! number: {number} boardid: {boardid} column: {col} winner boards count: {len(winlist)}")
                    print( calculate_board(board * int(number)))
                    bingo = True
                    winner_board = board
                    winner_boardid = boardid
                    winner_number = number
                    if len(boards.keys()) > len(winlist):
                        winlist.add(boardid)
                        bingo = False

    if bingo:
        if len(boards.keys()) == len(winlist):
            winner_board = board
            winner_boardid = boardid
            winner_number = number
            break
        else:
            break



# print_boards(boards)
print(f"the last winner board is {winner_boardid + 1} out of {number_of_boards}")
print_board(winner_board)
print_board(original[winner_boardid])
print(numbers)
print(int(winner_number))
print(calculate_board(winner_board))
print( calculate_board(winner_board) * int(winner_number))

