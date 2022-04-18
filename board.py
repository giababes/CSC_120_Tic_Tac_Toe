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
        board[row][col] = 'X'
    elif player_id == 2:
        board[row][col] = 'O'


def check_win(player_id):
    if player_id == 1:
        if (board[0][0] == board[0][1] == board[0][2] == 'X') or \
                (board[1][0] == board[1][1] == board[1][2] == 'X') or \
                (board[2][0] == board[2][1] == board[2][2] == 'X'): \
                return True
    else:
        return False

    if player_id == 2:
        if (board[0][0] == board[0][1] == board[0][2] == 'X') or \
                (board[1][0] == board[1][1] == board[1][2] == 'X') or \
                (board[2][0] == board[2][1] == board[2][2] == 'X'): \
                return True
    else:
        return False


def main():
    print("Testing print_board")
    print_board(board)

    print("Before place_mark, check_mark for 1, 1 is ", check_mark(1, 1))

    place_mark(1, 1, 1)
    print("After place_mark, check_mark for 1, 1, is", check_mark(1, 1))

    place_mark(0, 2, 2)

    place_mark(1, 2, 1)
    place_mark(1, 0, 1)
    print_board(board)

    print("Player 1 wins!", check_win(1))
    print("Player 2 wins!", check_win(2))


main()