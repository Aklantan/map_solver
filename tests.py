import unittest
from graphics import Maze

class Tests(unittest.TestCase):
    # def test_maze_create_cells(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_rows,
    #     )

    # def test_maze_create_cells1(self):
    #     num_cols = 29
    #     num_rows = 88
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_rows,
    #     )
    
    # def test_maze_create_cells2(self):
    #     num_cols = 3
    #     num_rows = 234
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_rows,
    #     )
    def test_reset_cells_visited(self):
        # Create a small test maze
        maze = Maze(0, 0, 2, 2, 10, 10)
    
        # Set all cells to visited = True first
        for row in maze._cells:
            for cell in row:
                cell._visited = True
            
        # Call the reset method
        maze._reset_cells_visited()
    
        # Verify all cells are now False
        for row in maze._cells:
            for cell in row:
                self.assertFalse(cell._visited)




if __name__ == "__main__":
    unittest.main()