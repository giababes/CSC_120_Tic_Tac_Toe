#this list contains 3 list, each of 3 elements, each element being a single character
board = []

#print the board as a 3x3 table
def print_board(): ...

#this function returns True if board [row][col] is currently unmarked,
#and thus can be chosen by a player. It returns False otherwise.
def check_mark(row, col):...

#This function changes board [row][col] to be marked by the given player.
#Player 1's mark is X, player 2's mark is O
def place_mark(row, col, player):...

#This function returns true if the indicated player has won the game.
#It returns false otherwise.
#For player 1, winning means that board has a completed row, column or
#diagonal of X.
#For player 2, winning means that board has a complete row, column or
#diagonal of 0.
def check_win(player):...

def main():
    print("Testing print_board")
    print_board()

    #print("Before place_mark, check_mark for 1, 1 is", check_mark91, 1))
    #
    #place_mark(1, 1, 1,)
    #print("after place_mark, check_work for 1, 1, is" check_mark 1,1,))
    #place_mark (0, 2, 2)
    #print_board()

main()