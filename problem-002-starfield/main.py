import random
import time
from tkinter import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_POS = '300+300'
STAR_SIZE = 4
INITIAL_NUMBER_OF_STARS = 10
REFRESH_RATE = 0.01

t = None

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def create_random_starfield():
    stars = []
    for i in range(INITIAL_NUMBER_OF_STARS):
        stars.append([random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)])
    return stars


def create_window():
    window = Tk()
    window.title("Starfield")
    window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_POS}')
    return window


def create_canvas(window):
    canvas = Canvas(window)
    canvas.configure(bg="black")
    canvas.pack(fill="both", expand=True)
    return canvas

def animate_stars(window, canvas, dx, dy):
    random_start_coords = create_random_starfield()
    canvas_stars = []
    for star_coords in random_start_coords:
        canvas_stars.append(canvas.create_oval(star_coords[0], star_coords[1], star_coords[0]+STAR_SIZE, star_coords[1]+STAR_SIZE, fill='white'))

    while True:
        for star in canvas_stars:
            canvas.move(star, dx, dy)

        window.update()
        time.sleep(REFRESH_RATE)


def run():
    animation_window = create_window()
    animation_canvas = create_canvas(animation_window)
    animate_stars(animation_window, animation_canvas, 1, 1)
    print(t)

    mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    run()
