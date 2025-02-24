import unittest
import numpy as np
from visualization.maze_renderer import MazeRenderer

class TestMazeRenderer(unittest.TestCase):
    def setUp(self):
        # create a small test maze array (3x3 with walls = 7x7)
        self.test_maze = np.ones((7, 7), dtype=np.int8)
        # create a simple path in the maze
        self.test_maze[1::2, 1::2] = 0  # make cells accessible
        self.test_maze[1, 2] = 0  # create a path between cells
        
        # create renderer with small cell size for testing
        self.renderer = MazeRenderer(cell_size=10)
    
    def test_initialization(self):
        """Test renderer initialization"""
        renderer = MazeRenderer(cell_size=15)
        
        # check if attributes were set correctly
        self.assertEqual(renderer.cell_size, 15)
        self.assertEqual(renderer.wall_color, (0, 0, 0))
        self.assertEqual(renderer.path_color, (255, 255, 255))
    
    def test_window_dimensions(self):
        """Test window dimension calculations"""
        # test maze is 7x7, cell_size is 10
        expected_width = 7 * 10  # width * cell_size
        expected_height = 7 * 10  # height * cell_size
        
        # create window (note: this will open a pygame window briefly)
        window = self.renderer.create_window(self.test_maze)
        
        # check dimensions
        actual_size = window.get_size()
        self.assertEqual(actual_size, (expected_width, expected_height))

if __name__ == '__main__':
    unittest.main() 