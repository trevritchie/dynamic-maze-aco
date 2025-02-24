import numpy as np

"""
This module implements a perfect maze generator using the Recursive Backtracking algorithm.

A perfect maze is one that has:
- Exactly one path between any two points
- No loops/cycles
- No isolated walls or unreachable areas

The Recursive Backtracking algorithm works by:
1. Starting at a cell and marking it as visited
2. While there are unvisited cells:
   a. Get all unvisited neighbors 2 cells away (skipping walls)
   b. If no unvisited neighbors, backtrack
   c. Otherwise:
      - Choose random unvisited neighbor
      - Remove wall between current cell and chosen neighbor
      - Move to chosen neighbor
      - Mark as visited
3. Repeat until all cells are visited

The grid is represented as a 2D numpy array where:
- 1 represents walls
- 0 represents paths
- Grid is (2n+1) x (2n+1) to account for walls between cells
"""

DEBUG = False  # for testing

class PerfectMaze:
    def __init__(self, width, height):
        """Initialize a maze with given dimensions.
        The maze is represented as a grid where:
        - 1 represents walls
        - 0 represents paths
        """
        self.width = width
        self.height = height
        # multiply by 2 and add 1 to account for walls between cells
        self.grid = np.ones((height * 2 + 1, width * 2 + 1), dtype=np.int8)
        
    def generate(self):
        """Generate a perfect maze using Recursive Backtracking algorithm."""
        # start from top-left corner (avoiding outer walls)
        begin_x, begin_y = (1, 1)
        # mark starting cell as path
        self.grid[begin_y, begin_x] = 0
        # stack keeps track of our path for backtracking
        stack = [(begin_x, begin_y)]
        # set of cells we've already visited
        visited = {(begin_x, begin_y)}
        
        while stack:
            current_x, current_y = stack[-1]
            # get cells we haven't visited yet that are 2 steps away
            neighbors = self._get_unvisited_neighbors(current_x, current_y)
            
            if not neighbors:
                # no unvisited neighbors = backtrack
                stack.pop()
                continue
                
            # randomly choose next cell to visit
            next_x, next_y = neighbors.pop()
            # knock down the wall between current and next cell
            wall_x = (current_x + next_x) // 2  # find wall x coordinate
            wall_y = (current_y + next_y) // 2  # find wall y coordinate
            self.grid[wall_y, wall_x] = 0  # remove wall
            self.grid[next_y, next_x] = 0  # mark next cell as path
            
            # add new cell to our path
            stack.append((next_x, next_y))
            visited.add((next_x, next_y))
            
        return self.grid
    
    def _get_unvisited_neighbors(self, x, y):
        """Get all unvisited neighboring cells."""
        neighbors = []
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # right, down, left, up
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 < new_x < self.width * 2 and 
                0 < new_y < self.height * 2 and 
                self.grid[new_y, new_x] == 1):
                neighbors.append((new_x, new_y))
            
        # randomly shuffle the neighbors
        indices = np.random.choice(len(neighbors), len(neighbors), replace=False)
        return [neighbors[i] for i in indices]  # Return list of coordinate tuples
    
    def is_perfect(self):
        """Validate if the maze is perfect (one path between any two points)."""
        # count cells that are paths (0s), excluding the walls between cells
        accessible = np.sum(self.grid[1::2, 1::2] == 0)  # only count actual cells, not walls
        expected = self.width * self.height
        
        # debug output
        if DEBUG:
            print(f"Grid shape: {self.grid.shape}")
            print(f"Accessible cells: {accessible}")
            print(f"Expected cells: {expected}")
            print(f"Grid:\n{self.grid}")
        
        return accessible == expected