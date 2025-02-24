import numpy as np

class ACOBehavior:
    """Handles Ant Colony Optimization behavior for agents."""
    
    def __init__(self, config=None):
        # Default config values - simplified
        self.config = {
            'pheromone_strength': 0.6,  # base intensity of pheromone deposits
            'max_pheromone': 1.0,       # upper limit for pheromone concentration
            'goal_influence': 5.0,      # weight of goal-directed behavior
            'pheromone_influence': 0.4,  # weight of pheromone trail following
            'backtrack_penalty': 0.1    # multiplier to discourage reversing direction
        }
        # Allow custom config to override defaults
        if config:
            self.config.update(config)
            
    def leave_pheromone(self, agent, maze_grid):
        """Leave pheromone trail as agent moves."""
        if hasattr(maze_grid, 'pheromone_grid'):
            # Scale pheromone by progress toward goal
            # More progress = stronger pheromone trail to reinforce good paths
            progress = 1 - (agent.current_distance / agent.initial_distance)
            strength = self.config['pheromone_strength'] * progress
            # Deposit pheromone at agent's current position
            maze_grid.pheromone_grid[agent.y, agent.x] += strength
            
    def follow_pheromones(self, agent, maze, temperature):
        """Calculate movement influence from pheromone trails."""
        # Fall back to random movement if maze doesn't support pheromones
        if not hasattr(maze, 'pheromone_grid'):
            return self._random_valid_move(agent, maze)
            
        moves = []  # stores possible (dx,dy) movement vectors
        values = [] # stores corresponding movement scores
        
        # Check all four cardinal directions
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:  # right, down, left, up
            new_x = agent.x + dx
            new_y = agent.y + dy
            # Only consider moves that don't hit walls
            if agent._is_valid_move(new_x, new_y, maze.grid):
                moves.append((dx, dy))
                
                # Calculate move score based on:
                # 1. Pheromone concentration at new position
                # 2. Whether move brings agent closer to goal
                value = (
                    maze.pheromone_grid[new_y, new_x] * self.config['pheromone_influence'] +
                    (2.0 if agent._is_closer_to_goal(new_x, new_y) else 0.5) * self.config['goal_influence']
                )
                
                # Reduce score if move reverses previous direction
                if agent.vx == -dx and agent.vy == -dy:
                    value *= self.config['backtrack_penalty']
                    
                # Add randomness scaled by temperature for exploration
                # Higher temperature = more random exploration
                value += np.random.random() * temperature * 2
                
                values.append(value)
        
        # If no valid moves found, stay in place
        if not moves:
            return 0, 0
            
        # Select the move with highest score
        best_idx = np.argmax(values)
        return moves[best_idx]
        
    def _random_valid_move(self, agent, maze):
        """Choose random valid move for exploration."""
        possible_moves = []
        # Check all cardinal directions for valid moves
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_x = agent.x + dx
            new_y = agent.y + dy
            if agent._is_valid_move(new_x, new_y, maze.grid):
                possible_moves.append((dx, dy))
        
        # Return random valid move if available, otherwise stay in place
        if possible_moves:
            return possible_moves[np.random.randint(len(possible_moves))]
        return 0, 0 