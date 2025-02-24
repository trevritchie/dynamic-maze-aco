from visualization.simulation import Simulation

def main():
    # Maze dimensions (each unit becomes 2 cells + walls)
    MAZE_WIDTH = 15      # Width of maze in units
    MAZE_HEIGHT = 12     # Height of maze in units
    
    # Agent settings
    NUM_AGENTS = 6       # Number of agents searching for goal
    
    # Dynamic maze settings
    WALL_CHANGE_INTERVAL = 60   # How often walls can change (frames between changes)
    WALL_CHANGE_PROBABILITY = 0.03  # Chance of each wall changing when update occurs
    
    # Simulation settings
    FPS = 15            # Frames per second (lower = slower simulation)
    SIMULATION_TIME = 20  # Maximum time in seconds before simulation ends
    
    # ACO (Ant Colony Optimization) parameters
    PHEROMONE_STRENGTH = 0.6    # Pheromone strength
    GOAL_INFLUENCE = 5.0        # Weight of goal direction in movement decisions
    PHEROMONE_INFLUENCE = 0.3   # Weight of pheromone trails in movement decisions
    BACKTRACK_PENALTY = 0.1     # Penalty for reversing direction (lower = stronger penalty)

    config = {
        # Simulation settings
        'maze_size': (MAZE_WIDTH, MAZE_HEIGHT),
        'num_agents': NUM_AGENTS,
        'wall_change_interval': WALL_CHANGE_INTERVAL,
        'wall_change_probability': WALL_CHANGE_PROBABILITY,
        'fps': FPS,
        'simulation_time': SIMULATION_TIME,
        
        # ACO behavior settings
        'aco': {
            'pheromone_strength': PHEROMONE_STRENGTH,
            'goal_influence': GOAL_INFLUENCE,
            'pheromone_influence': PHEROMONE_INFLUENCE,
            'backtrack_penalty': BACKTRACK_PENALTY,
        }
    }
    
    sim = Simulation(config)
    sim.run()

if __name__ == "__main__":
    main() 