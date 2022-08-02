import random
from tkinter import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_POS = '300+300'
STAR_SIZE = 2
INITIAL_NUMBER_OF_STARS = 10


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def create_random_starfield():
    stars = []
    for i in range(INITIAL_NUMBER_OF_STARS):
        stars.append([random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)])
    return stars


def run():
    root = Tk()
    root.title('Starfield')
    root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_POS}')
    canvas = Canvas(root, bg='black')
    canvas.pack()


    canvas.grid()
    for s in create_random_starfield():
        pass
        canvas.create_oval(s[0], s[1], s[0]+STAR_SIZE, s[1]+STAR_SIZE, fill='white')


    mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    run()
