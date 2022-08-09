from tkinter import Tk, Canvas, mainloop
SCALE = 2
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BLOCK_SIZE = 10
BLOCK_COLOR = '#000000'
WINDOW_POS = '300+300'


def create_game_window():
    window = Tk()
    window.title("Snake")
    window.geometry(f'{WINDOW_WIDTH*SCALE}x{WINDOW_HEIGHT*SCALE}+{WINDOW_POS}')


def create_game_canvas(window):
    canvas = Canvas(window)
    canvas.configure(bg="black")
    canvas.pack(fill="both", expand=True)
    return canvas




def run():
    game_window = create_game_window()
    game_canvas = create_game_canvas(game_window)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Snake Game')
    run()
    mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
