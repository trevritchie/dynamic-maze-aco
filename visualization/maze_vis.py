import pygame
import numpy as np

class MazeVisualizer:
    # Constants for display
    BACKGROUND_COLOR = (255, 255, 255)  # White
    WALL_COLOR = (0, 0, 0)             # Black
    AGENT_COLOR = (0, 0, 255)          # Blue
    PATH_COLOR = (0, 255, 0)           # Green
    GOAL_COLOR = (255, 0, 0)           # Red
    HUD_COLOR = (240, 240, 240)        # Light gray
    HUD_HEIGHT = 40                    # Height of HUD area

    def __init__(self, width, height, cell_size):
        pygame.init()
        self.width = width
        self.height = height + self.HUD_HEIGHT
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Multi-Agent Pathfinding")
        self.font = pygame.font.Font(None, 32)

    def draw(self, maze, agents, time_remaining, finish_time=None):
        self._draw_maze(maze)
        self._draw_agents(agents)
        self._draw_hud(time_remaining, finish_time, agents[0].temperature if agents else 0)
        pygame.display.flip()

    def _draw_maze(self, maze):
        """Draw maze grid with pheromone trails."""
        # Clear screen
        self.screen.fill(self.BACKGROUND_COLOR)
        
        # Draw HUD background
        pygame.draw.rect(self.screen, self.HUD_COLOR,
                        (0, 0, self.width, self.HUD_HEIGHT))
        
        # Draw walls with offset for HUD
        for y in range(maze.grid.shape[0]):
            for x in range(maze.grid.shape[1]):
                if maze.grid[y, x] == 1:
                    pygame.draw.rect(self.screen, self.WALL_COLOR,
                                  (x * self.cell_size, 
                                   y * self.cell_size + self.HUD_HEIGHT,
                                   self.cell_size, self.cell_size))
        
        # Draw pheromone trails with offset
        max_pher = np.max(maze.pheromone_grid)
        if max_pher > 0:
            for y in range(maze.grid.shape[0]):
                for x in range(maze.grid.shape[1]):
                    pher_level = maze.pheromone_grid[y, x]
                    if pher_level > 0:
                        dot_size = int(self.cell_size/4 * (pher_level / max_pher))
                        pygame.draw.circle(self.screen, 
                                        self.PATH_COLOR,
                                        (x * self.cell_size + self.cell_size//2,
                                         y * self.cell_size + self.cell_size//2 + self.HUD_HEIGHT),
                                        max(1, dot_size))

    def _draw_agents(self, agents):
        """Draw agents and goals with HUD offset."""
        for agent in agents:
            # Draw agent
            agent_pos = (agent.x * self.cell_size + self.cell_size//2,
                        agent.y * self.cell_size + self.cell_size//2 + self.HUD_HEIGHT)
            pygame.draw.circle(self.screen, self.AGENT_COLOR,
                             agent_pos, self.cell_size//3)
            
            # Draw goal (only once since it's shared)
            if agent == agents[0]:
                goal_pos = (agent.goal_x * self.cell_size + self.cell_size//2,
                          agent.goal_y * self.cell_size + self.cell_size//2 + self.HUD_HEIGHT)
                pygame.draw.circle(self.screen, self.GOAL_COLOR,
                                 goal_pos, self.cell_size//4)

    def _draw_hud(self, time_remaining, finish_time, temperature):
        """Draw countdown timer, temperature, and finish time."""
        # Draw timer in top left
        timer_text = f"Time: {int(time_remaining)}s"
        text_surface = self.font.render(timer_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, 10)
        self.screen.blit(text_surface, text_rect)
        
        # Draw finish time in top center if goal reached
        if finish_time is not None:
            finish_text = f"Finished in: {int(finish_time)}s"
            finish_surface = self.font.render(finish_text, True, (0, 150, 0))
            finish_rect = finish_surface.get_rect()
            finish_rect.midtop = (self.width // 2, 10)
            self.screen.blit(finish_surface, finish_rect)
        
        # Draw temperature in top right
        red = int(255 * temperature)
        blue = int(255 * (1 - temperature))
        temp_color = (red, 0, blue)
        
        temp_text = f"Temp: {temperature:.2f}"
        temp_surface = self.font.render(temp_text, True, temp_color)
        temp_rect = temp_surface.get_rect()
        temp_rect.topright = (self.width - 10, 10)
        self.screen.blit(temp_surface, temp_rect) 