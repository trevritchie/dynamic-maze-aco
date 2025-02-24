import pygame

class MazeRenderer:
    def __init__(self, cell_size=20):
        """Initialize the renderer with given cell size."""
        # init pygame before we do anything else
        pygame.init()
        # size of each cell in pixels
        self.cell_size = cell_size
        # colors for maze elements (using RGB values)
        self.wall_color = (0, 0, 0)  # black walls
        self.path_color = (255, 255, 255)  # white paths
        
    def create_window(self, maze_array):
        """Create a window sized to fit the maze."""
        # get maze dimensions from numpy array
        height, width = maze_array.shape
        # calculate pixel dimensions
        screen_width = width * self.cell_size
        screen_height = height * self.cell_size
        # create and return the game window
        return pygame.display.set_mode((screen_width, screen_height))
        
    def render(self, screen, maze_array):
        """Render the maze to the screen."""
        # fill screen with path color first
        screen.fill(self.path_color)
        
        # get dimensions for iteration
        height, width = maze_array.shape
        # draw each wall cell as a black rectangle
        for y in range(height):
            for x in range(width):
                if maze_array[y, x] == 1:  # wall cells are 1s
                    pygame.draw.rect(
                        screen,
                        self.wall_color,
                        (x * self.cell_size,  # x position in pixels
                         y * self.cell_size,  # y position in pixels
                         self.cell_size,      # width in pixels
                         self.cell_size)      # height in pixels
                    )
        
        # update the display to show changes
        pygame.display.flip() 