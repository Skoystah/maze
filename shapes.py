class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point at ({self.x}, {self.y})"


class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point_a.x,
            self.point_a.y,
            self.point_b.x,
            self.point_b.y,
            fill=fill_color,
            width=2,
        )

    def __repr__(self):
        return f"Line from {self.point_a} to {self.point_b}"


class Cell:
    def __init__(self, top_left, bottom_right, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = top_left.x
        self.__x2 = bottom_right.x
        self.__y1 = top_left.y
        self.__y2 = bottom_right.y
        self.__win = window

    def draw(self):
        if self.has_left_wall:
            wall = Line(Point(self.__x1, self.__y1),
                        Point(self.__x1, self.__y2))
            self.__win.draw_line(wall, "green")
        if self.has_bottom_wall:
            wall = Line(Point(self.__x1, self.__y2),
                        Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "green")
        if self.has_top_wall:
            wall = Line(Point(self.__x1, self.__y1),
                        Point(self.__x2, self.__y1))
            self.__win.draw_line(wall, "green")
        if self.has_right_wall:
            wall = Line(Point(self.__x2, self.__y1),
                        Point(self.__x2, self.__y2))
            self.__win.draw_line(wall, "green")

    def draw_move(self, to_cell, undo=False):
        move = Line(
            Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2),
            Point(
                (to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2
            ),
        )
        if undo:
            fill_color = "red"
        else:
            fill_color = "gray"

        self.__win.draw_line(move, fill_color)
