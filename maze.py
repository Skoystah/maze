from shapes import Point, Line
import time
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = self.__create_cells()
        self.__break_entrance_and_exit()

        if seed:
            random.seed(seed)

        self.__break_walls(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        cells = [[] for col in range(self.__num_cols)]
        cur_x = self.__x1
        cur_y = self.__y1

        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                cells[col].append(
                    Cell(
                        Point(cur_x, cur_y),
                        Point(cur_x + self.__cell_size_x,
                              cur_y + self.__cell_size_y),
                        self.__win,
                    )
                )
                cur_y += self.__cell_size_y  # move down a row
            cur_y = self.__y1  # back to first row
            cur_x += self.__cell_size_x  # move up one column

        # insert draw cell
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(cells[col][row])
        return cells

    def __draw_cell(self, cell):
        if not self.__win:
            return

        cell.draw()
        self.__animate()

    def __animate(self):
        if not self.__win:
            return

        self.__win.redraw()
        # time.sleep(0.01)

    def __break_entrance_and_exit(self):
        entrance = self.__cells[0][0]
        entrance.has_top_wall = False
        entrance.draw()

        exit_cell = self.__cells[self.__num_cols - 1][self.__num_rows - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    def __break_walls(self, i, j):
        self.__cells[i][j].visited = True
        current = self.__cells[i][j]

        while True:
            to_visit = []

            if i > 0:
                if not self.__cells[i - 1][j].visited:
                    to_visit.append((i - 1, j, "left"))
            if i < self.__num_cols - 1:
                if not self.__cells[i + 1][j].visited:
                    to_visit.append((i + 1, j, "right"))
            if j > 0:
                if not self.__cells[i][j - 1].visited:
                    to_visit.append((i, j - 1, "up"))
            if j < self.__num_rows - 1:
                if not self.__cells[i][j + 1].visited:
                    to_visit.append((i, j + 1, "down"))

            if not to_visit:
                current.draw()
                return

            new_i, new_j, dir = to_visit[random.randint(0, len(to_visit) - 1)]

            match dir:
                case "left":
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[new_i][new_j].has_right_wall = False
                case "right":
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[new_i][new_j].has_left_wall = False
                case "up":
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[new_i][new_j].has_bottom_wall = False
                case "down":
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[new_i][new_j].has_top_wall = False

            self.__break_walls(new_i, new_j)

    def __reset_cells_visited(self):
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__cells[col][row].visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True
        current = self.__cells[i][j]

        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True

        to_visit = []

        if i > 0:
            if (
                not self.__cells[i - 1][j].visited
                and not self.__cells[i][j].has_left_wall
                and not self.__cells[i - 1][j].has_right_wall
            ):
                to_visit.append((i - 1, j, "left"))
        if i < self.__num_cols - 1:
            if (
                not self.__cells[i + 1][j].visited
                and not self.__cells[i][j].has_right_wall
                and not self.__cells[i + 1][j].has_left_wall
            ):
                to_visit.append((i + 1, j, "right"))
        if j > 0:
            if (
                not self.__cells[i][j - 1].visited
                and not self.__cells[i][j].has_top_wall
                and not self.__cells[i][j - 1].has_bottom_wall
            ):
                to_visit.append((i, j - 1, "up"))
        if j < self.__num_rows - 1:
            if (
                not self.__cells[i][j + 1].visited
                and not self.__cells[i][j].has_bottom_wall
                and not self.__cells[i][j + 1].has_top_wall
            ):
                to_visit.append((i, j + 1, "down"))

        for new_i, new_j, dir in to_visit:
            self.__cells[i][j].draw_move(self.__cells[new_i][new_j])
            time.sleep(0.20)
            if self.__solve_r(new_i, new_j):
                return True
            self.__cells[i][j].draw_move(
                self.__cells[new_i][new_j], True)  # Undo
            time.sleep(0.20)
        return False


class Cell:
    def __init__(self, top_left, bottom_right, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = top_left.x
        self.__x2 = bottom_right.x
        self.__y1 = top_left.y
        self.__y2 = bottom_right.y
        self.__win = window

    def draw(self):
        if not self.__win:
            return

        left_wall = Line(Point(self.__x1, self.__y1),
                         Point(self.__x1, self.__y2))
        if self.has_left_wall:
            self.__win.draw_line(left_wall, "green")
        else:
            self.__win.draw_line(left_wall, "white")

        bottom_wall = Line(Point(self.__x1, self.__y2),
                           Point(self.__x2, self.__y2))
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall, "green")
        else:
            self.__win.draw_line(bottom_wall, "white")

        top_wall = Line(Point(self.__x1, self.__y1),
                        Point(self.__x2, self.__y1))
        if self.has_top_wall:
            self.__win.draw_line(top_wall, "green")
        else:
            self.__win.draw_line(top_wall, "white")

        right_wall = Line(Point(self.__x2, self.__y1),
                          Point(self.__x2, self.__y2))
        if self.has_right_wall:
            self.__win.draw_line(right_wall, "green")
        else:
            self.__win.draw_line(right_wall, "white")

    def draw_move(self, to_cell, undo=False):
        if not self.__win:
            return

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
