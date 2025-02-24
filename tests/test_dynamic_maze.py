import unittest
import numpy as np
from maze.dynamic_maze import DynamicMaze

class TestDynamicMaze(unittest.TestCase):
    def setUp(self):
        self.maze = DynamicMaze(5, 5, change_probability=1.0)  # 100% change for testing
        self.maze.generate()
    
    def test_mutable_walls_identified(self):
        """Test that mutable walls are identified correctly"""
        # should have walls to mutate
        self.assertTrue(len(self.maze.changeable_walls) > 0)
        
        # check that no outer walls are included
        for x, y in self.maze.changeable_walls:
            self.assertTrue(0 < x < self.maze.width * 2)
            self.assertTrue(0 < y < self.maze.height * 2)
    
    def test_wall_updates(self):
        """Test that walls change when updated"""
        # store initial state
        initial_state = self.maze.grid.copy()
        
        # update maze
        self.maze.update()
        
        # check that some walls changed
        self.assertTrue(np.any(initial_state != self.maze.grid))
        
        # check that outer walls didn't change
        self.assertTrue(np.all(self.maze.grid[0, :] == 1))  # top
        self.assertTrue(np.all(self.maze.grid[-1, :] == 1))  # bottom
        self.assertTrue(np.all(self.maze.grid[:, 0] == 1))  # left
        self.assertTrue(np.all(self.maze.grid[:, -1] == 1))  # right

if __name__ == '__main__':
    unittest.main() 