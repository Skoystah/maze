from window import Window
from shapes import Point
from maze import Maze, Cell


def main():
    win = Window(800, 600)
    # line = Line(Point(6, 6), Point(150, 150))
    # line2 = Line(Point(150, 150), Point(300, 450))
    # line3 = Line(Point(300, 450), Point(600, 200))

    # win.draw_line(line, "red")
    # win.draw_line(line2, "blue")
    # win.draw_line(line3, "green")

    # cell = Cell(Point(6, 6), Point(56, 56), win)
    # cell2 = Cell(Point(106, 106), Point(156, 156), win)
    # cell3 = Cell(Point(286, 286), Point(336, 336), win)
    # cell.draw()
    # cell2.draw()
    # cell3.draw()
    # cell.draw_move(cell2)
    # cell2.draw_move(cell3, True)

    maze = Maze(6, 6, 10, 10, 20, 20, win, None)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
