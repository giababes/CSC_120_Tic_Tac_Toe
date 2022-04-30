board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]


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
                (board[2][0] == board[2][1] == board[2][2] == 'X') or \
                (board[0][0] == board[1][0] == board[2][0] == 'X') or \
                (board[0][1] == board[1][1] == board[2][1] == 'X') or \
                (board[0][2] == board[1][2] == board[2][2] == 'X') or \
                (board[0][0] == board[1][1] == board[2][2] == 'X') or \
                (board[0][2] == board[1][1] == board[2][0] == 'X'):
            return True

        else:
            return False

    if player_id == 2:
        if (board[0][0] == board[0][1] == board[0][2] == 'O') or \
                (board[1][0] == board[1][1] == board[1][2] == 'O') or \
                (board[2][0] == board[2][1] == board[2][2] == 'O') or \
                (board[0][0] == board[1][0] == board[2][0] == 'O') or \
                (board[0][1] == board[1][1] == board[2][1] == 'O') or \
                (board[0][2] == board[1][2] == board[2][2] == 'O') or \
                (board[0][0] == board[1][1] == board[2][2] == 'O') or \
                (board[0][2] == board[1][1] == board[2][0] == 'O'):
            return True
        else:
            return False


def main():
    row_choice = 0
    col_choice = 0
    player_won = False
    winning_player = 0

    #  print("Testing print_board")
    #  print_board(board)
    print("Tic-Tac-Toe!")
    print("Player 1 is X, Player 2 is O.")
    while not player_won:
        for player in range(1, 3):
            row_choice = int(input("Player " + str(player) + " make your move. Choose your row: "))
            while row_choice not in range(0, 3):
                row_choice = int(input("Error: Row number must be 0, 1, or 2. Please re-enter number: "))
            col_choice = int(input("Player " + str(player) + " choose your col: "))
            while col_choice not in range(0, 3):
                col_choice = int(input("Error: Column number must be 0, 1, or 2. Please re-enter number: "))
            while check_mark(row_choice, col_choice) is False:
                print("Invalid move, this location has already been selected. Please move again.")
                row_choice = int(input("Player " + str(player) + " make your move. Choose your row: "))
                col_choice = int(input("Player " + str(player) + " choose your col: "))

            place_mark(row_choice, col_choice, player)
            print_board(board)


main()