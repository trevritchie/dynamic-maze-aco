import numpy as np
from maze.perfect_maze import PerfectMaze

class DynamicMaze(PerfectMaze):
    def __init__(self, width, height, change_probability=0.01):
        """Initialize a dynamic maze."""
        super().__init__(width, height)
        self.change_probability = change_probability
        # keep track of walls that can change (not outer walls)
        self.changeable_walls = []
        
        # Add pheromone grid
        self.pheromone_grid = np.zeros((height * 2 + 1, width * 2 + 1))
        self.evaporation_rate = 0.85  # Increased evaporation from 0.90
        
    def generate(self):
        """Generate initial maze and identify changeable walls."""
        maze = super().generate()
        self._identify_changeable_walls()
        return maze
        
    def _identify_changeable_walls(self):
        """Find all walls that could potentially change."""
        self.changeable_walls = []
        # skip outer walls by checking inner grid points
        for y in range(1, self.height * 2):
            for x in range(1, self.width * 2):
                if self.grid[y, x] == 1:  # if it's a wall
                    self.changeable_walls.append((x, y))
    
    def update(self):
        """Update maze and decay pheromones."""
        # Update walls
        for y in range(1, self.grid.shape[0] - 1):
            for x in range(1, self.grid.shape[1] - 1):
                if np.random.random() < self.change_probability:
                    # Only change walls, not paths
                    if self.grid[y, x] == 1:
                        self.grid[y, x] = 0
                    elif all(self.grid[ny, nx] == 0 for ny, nx in self._get_neighbors(y, x)):
                        self.grid[y, x] = 1
                        
        # Decay pheromones
        # print("\nDecaying pheromones")
        # print(f"Before decay - Max: {np.max(self.pheromone_grid)}, Mean: {np.mean(self.pheromone_grid)}")
        self.pheromone_grid *= self.evaporation_rate
        # print(f"After decay - Max: {np.max(self.pheromone_grid)}, Mean: {np.mean(self.pheromone_grid)}")

    def _get_neighbors(self, y, x):
        """Get valid neighboring cells."""
        neighbors = []
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = y + dy, x + dx
            if (0 <= ny < self.grid.shape[0] and 
                0 <= nx < self.grid.shape[1]):
                neighbors.append((ny, nx))
        return neighbors 