import pygame
import numpy as np
from visualization.maze_vis import MazeVisualizer
from agents.agent import Agent
from maze.dynamic_maze import DynamicMaze

class Simulation:
    # Constants
    CELL_SIZE = 20  # Fixed cell size for consistent visualization

    def __init__(self, config=None):
        # default configuration
        if config is None:
            self.config = {
                'maze_size': (10, 10),
                'num_agents': 5,
                'wall_change_interval': 60,  # 2 seconds at 30fps
                'wall_change_probability': 0.01,
                'fps': 30,
                'simulation_time': 20,
            }
        else:
            self.config = config

        # Initialize components
        self._init_simulation()

    def _init_simulation(self):
        width, height = self.config['maze_size']
        self.grid_width = width * 2 + 1
        self.grid_height = height * 2 + 1
        
        # Create maze and visualization
        self.maze = DynamicMaze(width, height, self.config['wall_change_probability'])
        self.maze.generate()
        
        window_width = self.grid_width * self.CELL_SIZE
        window_height = self.grid_height * self.CELL_SIZE
        self.visualizer = MazeVisualizer(window_width, window_height, self.CELL_SIZE)
        
        # Initialize agents and timing
        self.goal_pos = self._select_goal()
        self.agents = self._create_agents()
        self.clock = pygame.time.Clock()
        self.frame_count = 0
        self.time_remaining = self.config['simulation_time']
        self.finish_time = None
        self.start_time = None

    def _select_goal(self):
        empty_cells = []
        min_goal_x = self.grid_width // 2  # Goal must be at least halfway across

        for y in range(1, self.grid_height, 2):
            for x in range(min_goal_x, self.grid_width, 2):  # Start from halfway
                if self.maze.grid[y, x] == 0:
                    empty_cells.append((x, y))

        if empty_cells:  # Make sure we found valid cells
            goal_idx = np.random.randint(len(empty_cells))
            return empty_cells[goal_idx]
        else:  # Fallback to rightmost empty cell if no valid cells found
            for y in range(1, self.grid_height, 2):
                for x in range(self.grid_width-2, min_goal_x-1, -2):
                    if self.maze.grid[y, x] == 0:
                        return (x, y)

    def _create_agents(self):
        """Create agents starting from a 'colony' position."""
        agents = []
        
        colony_cells = []
        for y in range(1, self.grid_height - 1, 2):
            for x in range(1, 3, 2):
                if self.maze.grid[y, x] == 0:
                    colony_cells.append((x, y))
        
        colony_pos = colony_cells[np.random.randint(len(colony_cells))]
        
        # Combine agent and ACO configs
        agent_config = {
            'simulation_time': self.config['simulation_time'],
            'min_temperature': 0.01,
            'initial_temperature': 1.0,
        }
        
        # Add ACO config if provided
        if 'aco' in self.config:
            agent_config['aco'] = self.config['aco']
        
        for _ in range(self.config['num_agents']):
            agent = Agent(colony_pos[0], colony_pos[1], 
                         self.goal_pos[0], self.goal_pos[1],
                         config=agent_config)
            agents.append(agent)
        
        return agents

    def _handle_events(self):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        return running

    def _update_simulation(self):
        # Update maze periodically
        if self.frame_count % self.config['wall_change_interval'] == 0:
            self.maze.update()
        
        # Update agents
        self.maze.agents = self.agents
        for agent in self.agents:
            agent.move(self.maze, self.agents, self.time_remaining)
            # Check if any agent reached the goal
            if agent.x == agent.goal_x and agent.y == agent.goal_y:
                if self.finish_time is None:  # Only record first finish
                    elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
                    self.finish_time = elapsed

        # Increment frame count
        self.frame_count += 1

    def run(self):
        running = True
        self.start_time = pygame.time.get_ticks()
        
        while running:
            # Handle timing
            current_time = pygame.time.get_ticks()
            elapsed_seconds = (current_time - self.start_time) / 1000
            self.time_remaining = max(0, self.config['simulation_time'] - elapsed_seconds)
            
            # Handle events
            running = self._handle_events()
            
            # Update simulation
            self._update_simulation()
            
            # Draw current state
            self.visualizer.draw(self.maze, self.agents, self.time_remaining, self.finish_time)
            
            # Control frame rate
            self.clock.tick(self.config['fps']) 