from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(
            self.__root, bg="white", height=self.__height, width=self.__width
        )
        self.__canvas.pack(expand=1, fill=BOTH)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
