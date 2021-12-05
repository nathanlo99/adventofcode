
import sys

from pprint import pprint

numbers = list(map(int, input().split(",")))

EMPTY = -1


def completed(board):
    return [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY] in board or any(all(row[i] == EMPTY for row in board) for i in range(5))


def get_raw_score(board):
    return sum(sum(thing for thing in row if thing != EMPTY) for row in board)


def mark_number(board, num):
    for row_i, row in enumerate(board):
        if num in row:
            new_row = [EMPTY if thing == num else thing for thing in row]
            new_board = board[:row_i] + [new_row] + board[row_i + 1:]
            return new_board, True
    return board, False


boards = []
while True:
    try:
        input()
    except:
        break
    lines = [list(map(int, input().split())) for _ in range(5)]
    boards.append(lines)

for num in numbers:
    new_boards = []
    for board in boards:
        new_board, added = mark_number(board, num)
        if added and completed(new_board):
            print(num * get_raw_score(new_board))
            new_board = [[EMPTY for _ in range(5)] for __ in range(5)]
        new_boards.append(new_board)
    boards = new_boards
