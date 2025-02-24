import unittest
import numpy as np
from maze.perfect_maze_generator import PerfectMaze

class TestPerfectMaze(unittest.TestCase):
    def setUp(self):
        """setup runs before each test"""
        # create a small 5x5 maze for testing
        self.maze = PerfectMaze(5, 5)
        
    def test_maze_dimensions(self):
        """test if maze dimensions are correct (including walls)"""
        # maze should be (2n + 1) x (2n + 1) where n is the input dimension
        expected_height = 11  # 2*5 + 1
        expected_width = 11   # 2*5 + 1
        self.assertEqual(self.maze.grid.shape, (expected_height, expected_width))
        
    def test_maze_initialization(self):
        """test if maze is initially all walls"""
        # all cells should be 1 (walls) after initialization
        self.assertTrue(np.all(self.maze.grid == 1))
        
    def test_maze_generation(self):
        """test various properties of generated maze"""
        maze_array = self.maze.generate()
        
        # test outer walls are intact
        self.assertTrue(np.all(maze_array[0, :] == 1))  # top wall
        self.assertTrue(np.all(maze_array[-1, :] == 1))  # bottom wall
        self.assertTrue(np.all(maze_array[:, 0] == 1))  # left wall
        self.assertTrue(np.all(maze_array[:, -1] == 1))  # right wall
        
        # test if maze is perfect (exactly width*height path cells)
        self.assertTrue(self.maze.is_perfect())
        
    def test_different_sizes(self):
        """test if maze generator works with different dimensions"""
        # test a few different sizes
        sizes = [(3, 3), (10, 10), (5, 10)]
        
        for width, height in sizes:
            with self.subTest(width=width, height=height):
                maze = PerfectMaze(width, height)
                maze_array = maze.generate()
                # check if dimensions are correct
                self.assertEqual(maze_array.shape, (height*2 + 1, width*2 + 1))
                # check if maze is perfect
                self.assertTrue(maze.is_perfect())

if __name__ == '__main__':
    unittest.main() 