import random
import time
from tkinter import Tk, Canvas, mainloop
SCALE = 2
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BLOCK_SIZE = 10
BLOCK_COLOR = "#EE4035"
WINDOW_POS = '300+300'
REFRESH_RATE = 100


class SnakeGame:

    def __init__(self, window: Tk, canvas: Canvas):
        self.window = window
        self.canvas = canvas
        self.canvas.pack()
        self.last_key = 'up'
        self.initialise_snake()
        self.window.bind("<Key>", self.key_input)
        self.window.mainloop()

    def key_input(self, event):
        key_pressed = event.keysym
        print(key_pressed)
        self.last_key = key_pressed
        return key_pressed

    def play(self):
        print('play()')
        while True:
            self.window.update()
            #self.window.after(REFRESH_RATE, self.update_snake(self.last_key))
            print('>')


    def update_snake(self, last_key):
        direction = self.get_direction(self.last_key)
        print(direction)
        self.canvas.move(self.snake, 10, 0)

    def initialise_snake(self, initial_pos=None):
        if initial_pos is None:
            initial_pos = (random.randint(20,100),random.randint(20, 100))
        self.snake = self.canvas.create_rectangle(initial_pos[0], initial_pos[1], initial_pos[0] + BLOCK_SIZE * SCALE, initial_pos[1] + BLOCK_SIZE * SCALE,
                                                  fill=BLOCK_COLOR)
        self.nake_position = initial_pos


    def get_direction(self, last_key):
        if last_key == 'w':
            return 'up'
        if last_key == 's':
            return 'down'
        if last_key == 'a':
            return 'left'
        if last_key == 'd':
            return 'right'

        return None


def create_game_window():
    window = Tk()
    window.title("Snake")
    window.geometry(f'{WINDOW_WIDTH*SCALE}x{WINDOW_HEIGHT*SCALE}+{WINDOW_POS}')
    return window

def create_game_canvas(window):
    canvas = Canvas(window)
    canvas.configure(bg="black")
    canvas.pack(fill="both", expand=True)
    return canvas


def move_snake(movement_direction):
    print('move snake')
    if movement_direction == 'left':
        print('go left')
        return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Snake Game')
    game_window = create_game_window()
    game_canvas = create_game_canvas(game_window)
    
    game = SnakeGame(game_window, game_canvas)
    game.play()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
