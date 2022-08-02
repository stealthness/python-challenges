"""
This code creates a game for two human players to player Tic Tak Toe using a
simple commandline text based graphics display
"""


def print_board(board):
    """
    Prints the board state a command line text based graphic
    :param board:
    :return:
    """
    for i in range(3):
        print(f"{board[3*i+0]} | {board[3*i+1]} | {board[3*i+2]}")
        if i > 1:
            return
        print(f'- - - - -')


def print_position_selection():
    """
    Prints the board position numbers a command line text based graphic
    :return:
    """
    print_board([str(i+1) for i in range(9)])


def if_valid_move(board, move_selection, player_mark):
    if board[move_selection - 1] == '.':
        board[move_selection - 1] = player_mark
        return True

    return False


def make_move(board, player_mark: str):
    """
    Ask for player move, checks validity, also exits program if 'exit' is typed
    :param board:
    :param player_mark:
    :return:
    """
    while True:
        move_selection = input(f'player{player_mark} select your move')
        if move_selection == 'exit':
            exit(0)

        if if_valid_move(board, int(move_selection), player_mark):
            return

        print('not a valid move, try again')


def is_game_over(board):
    """
    Returns True if all the spaces are filled. Does not determine if the game ended by victory
    :param board:
    :return:
    """
    for s in board:
        if s == '.':
            return False
    return True


def has_player_won(board, player_mark):
    """
    Check the board to see if player_mark has won
    :param board:
    :param player_mark:
    :return:
    """
    mark_line = [player_mark]*3
    for i in range(3):
        # checks horizontal
        if [board[i*3], board[i*3+1], board[i*3+2]] == mark_line:
            return True
        # checks the vertical
        if [board[i], board[3+i], board[6+i]] == mark_line:
            return True
    # check the diagonals
    if [board[0], board[4], board[8]] == mark_line or [board[2], board[4], board[6]] == mark_line:
        return True

    return False


def print_welcome(board):
    print('Welcome to Tic Tac Toe Game (Noughts and Crosses)\n')
    print('Select position using:')
    print_position_selection()
    print('')




def play_game():
    # create an empty board
    board = ['.']*9
    print_welcome(board)
    while True:
        make_move(board, 'O')
        print_board(board)
        if has_player_won(board, 'O'):
            print(f'PlayerO has won')
            return
        if is_game_over(board):
            return
        make_move(board, 'X')
        print_board(board)
        if has_player_won(board, 'X'):
            print(f'PlayerX has won')
            return
        if is_game_over(board):
            return


if __name__ == '__main__':
    play_game()

