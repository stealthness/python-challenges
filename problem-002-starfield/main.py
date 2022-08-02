from tkinter import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_POS = '300+300'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def run():
    ws = Tk()

    ws.title('Starfield')
    ws.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_POS}')
    mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    run()

