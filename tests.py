import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_size(self):
        num_cols = 10
        num_rows = 15
        x1 = 0
        y1 = 0
        m2 = Maze(x1, y1, num_rows, num_cols, 10, 10)

        self.assertEqual(
            m2._Maze__cells[num_cols - 1][num_rows - 1]._Cell__x2, x1 + 10 * num_cols
        )
        self.assertEqual(
            m2._Maze__cells[num_cols - 1][num_rows - 1]._Cell__y2, y1 + 10 * num_rows
        )

    def test_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(m3._Maze__cells[0][0].has_top_wall, False)
        self.assertEqual(
            m3._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall, False
        )

    def test_reset_cells_visited(self):
        num_cols = 10
        num_rows = 10
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m4._Maze__cells:
            for cell in col:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
