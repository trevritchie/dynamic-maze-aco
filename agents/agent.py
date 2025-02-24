import numpy as np
from .aco import ACOBehavior

class Agent:
    """
    Implements a swarm-based agent using flocking behavior rules:
    - Separation: maintain safe distance from other agents
    - Alignment: match velocity with nearby agents
    - Cohesion: move toward center of local group
    Plus goal-seeking behavior for maze navigation
    """
    def __init__(self, x, y, goal_x, goal_y, config=None):
        # Default config values
        self.config = {
            'simulation_time': 20,
            'min_temperature': 0.01,
            'initial_temperature': 1.0,
        }
        if config:
            self.config.update(config)
        
        # Position and goal
        self.x = x
        self.y = y
        self.goal_x = goal_x
        self.goal_y = goal_y
        self.vx = self.vy = 0
        
        # Temperature for simulated annealing
        self.temperature = self.config['initial_temperature']
        self.min_temperature = self.config['min_temperature']
        
        # Distance tracking
        self.initial_distance = self._manhattan_distance(x, y, goal_x, goal_y)
        self.current_distance = self.initial_distance
        
        # Initialize ACO behavior with ACO config if provided
        aco_config = self.config.get('aco', None)
        self.aco = ACOBehavior(aco_config)
        
    def move(self, maze, agents, time_remaining):
        # Update temperature based on remaining time
        self.temperature = max(
            self.min_temperature,
            self.config['initial_temperature'] * (time_remaining / self.config['simulation_time'])
        )
        
        # Update current distance
        self.current_distance = self._manhattan_distance(self.x, self.y, self.goal_x, self.goal_y)
        
        # Check if reached goal
        if self.current_distance == 0:
            self.vx = self.vy = 0
            return
            
        # Get movement from ACO behavior
        self.vx, self.vy = self.aco.follow_pheromones(self, maze, self.temperature)
        
        # Apply movement if valid
        new_x = self.x + round(self.vx)
        new_y = self.y + round(self.vy)
        
        if self._is_valid_move(new_x, new_y, maze.grid):
            self.x = new_x
            self.y = new_y
            self.aco.leave_pheromone(self, maze)
        else:
            self.vx = self.vy = 0
        
    def _is_valid_move(self, x, y, maze_grid):
        """Check if position is valid and not a wall."""
        return (0 <= x < maze_grid.shape[1] and 
                0 <= y < maze_grid.shape[0] and 
                maze_grid[y, x] == 0)
                
    def _is_closer_to_goal(self, x, y):
        """Check if new position is closer to goal."""
        curr_dist = abs(self.x - self.goal_x) + abs(self.y - self.goal_y)
        new_dist = abs(x - self.goal_x) + abs(y - self.goal_y)
        return new_dist < curr_dist
    
    def _manhattan_distance(self, x1, y1, x2, y2):
        """Calculate Manhattan distance between two points."""
        return abs(x1 - x2) + abs(y1 - y2) 