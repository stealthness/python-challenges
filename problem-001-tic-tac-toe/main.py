# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_board(board):
    for i in range(3):
        print(f"{board[3*i+0]} | {board[3*i+0]} | {board[3*i+0]}")
        if i > 1:
            return
        print(f'- - - - -')


def play_game():
    print('Start game\n')
    board = ['.']*9
    print_board(board)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    play_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
