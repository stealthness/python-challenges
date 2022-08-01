# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_board(board):
    for i in range(3):
        print(f"{board[3*i+0]} | {board[3*i+1]} | {board[3*i+2]}")
        if i > 1:
            return
        print(f'- - - - -')


def print_position_selection():
    for i in range(3):
        print(f"{3 * i + 1} | {3 * i + 2} | {3 * i + 3}")
        if i > 1:
            return
        print(f'- - - - -')


def if_valid_move(move_selection):
    # not a complete function
    return move_selection == '1'


def make_move(player_no: int):
    valid_move = False
    while not valid_move:
        move_selection = input(f'player{player_no} select your move')

        if if_valid_move(move_selection):
            return
        else:
            print('not a valid move')

def play_game():
    print('Start game\n')
    board = ['.']*9
    print_board(board)
    print('Select position using:')
    print_position_selection()
    make_move(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    play_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
