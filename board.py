from typing import List

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]


# print the board as a 3x3 table
def print_board(board):
    for row in board:
        print(row)


def check_mark(row, col):
    if board[row][col] == '-':
        return True
    else:
        return False


def place_mark(row, col, player_id):
    if player_id == 1:
        board[row][col] == 'X'
    if player_id == 2:
        board[row][col] == 'O'


# def check_win(player_id):
#  for row in board:
#    if player_id == 1 and len(set(row)) == 1:
#      return row[0]
#  return -1


def main():
    print("Testing print_board")
    print_board(board)

    print("Before place_mark, check_mark for 1, 1 is ", check_mark(1, 1))

    place_mark(1, 1, 1)
    print("after place_mark, check_mark for 1, 1, is", check_mark(1, 1))
    # place_mark (0, 2, 2)
    # print_board()


main()