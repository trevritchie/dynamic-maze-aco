# Dynamic Multi-Agent Pathfinding in an Evolving Maze with Swarm Intelligence - Project Report
---

## Project Overview
This project implements a multi-agent pathfinding system in a dynamic maze environment using Ant Colony Optimization (ACO) for swarm intelligence. The agents navigate through a perfect maze that evolves over time, with walls opening and closing during simulation, requiring continuous path adaptation.

## Design Choices

### Architecture
The project follows a modular design with three core components:
- **Maze Generation**: Implements maze creation and dynamic modifications
- **Multi-Agent System**: Handles ACO-based swarm intelligence and agent behaviors
- **Visualization**: Provides real-time simulation display and user interaction

### Technology Stack
- **Python**: Primary programming language
- **Pygame**: Real-time visualization framework
- **NumPy**: Efficient matrix operations for maze representation

## Implementation Details

### Maze Generation
- Recursive Backtracking algorithm for maze creation
- Dynamic wall modification system for runtime changes
- Grid-based representation using NumPy arrays

### Swarm Intelligence Implementation
1. **Agent Behavior**
   - Collaborative navigation using ACO
   - Dynamic path adaptation to maze changes
   - Temperature-based exploration/exploitation balance
   - Pheromone-guided movement
   - Dynamic path adaptation to maze changes

2. **Pheromone System**
   - Collective intelligence through pheromone trails
   - Evaporation mechanics for path optimization
   - Grid-based pheromone tracking

### Visualization System
- Real-time maze rendering with Pygame
- Pheromone trail visualization
- Interactive wall modification
- Performance metrics display:
  - Time remaining
  - Temperature
  - Completion time (when finished)

## Parameter Tuning Journey

### Challenges Faced
1. **Core Difficulties**
   - Balancing exploration vs exploitation
   - Conflicting parameter influences
   - Difficulty telling exactly what parameter changes did

2. **Technical Challenges**
   - Pheromone management in dynamic environments
   - Pheremone grid

### Parameter Changed Over Time

1. **Removed Features**
   - Agent Memory: Removed due to complexity and overhead
   - We tried to remember the last 5 moves to stop repeating moves but we didn't get it to work

2. **Final Parameters**
   - We used temperature along with ACO, which maybe was not the right decision

   - Core Settings:
     - Temperature decay rate: 0.995
     - Pheromone evaporation: 0.1
     - Initial temperature: 1.0
     - Backtrack penalty: 0.1

   - Movement Weights:
     - Pheromone influence: 0.4
     - Goal influence: 5.0
     - Pheromone strength: 0.6
     - Max pheromone: 1.0

### Design Goals
We aimed to make agents:
- Maintain forward progress
- Explore new paths when needed
- Avoid getting stuck in loops
- Still allows backtracking when no better options exist

### Visualizatoin Decisions
- Make pheromones represented as green dots, and get bigger when stronger
- Make agents blue dots
- Make goal a red dot
- Make walls black
- Display time, temperature, and completion time
- Time changes from red to blue as temperature goes down

## References

1. Project Requirements Document

2. Ant Colony Optimization
   - [Introduction to Ant Colony Optimization](https://www.geeksforgeeks.org/introduction-to-ant-colony-optimization/)
   - [Optimization Algorithms in Machine Learning](https://www.geeksforgeeks.org/optimization-algorithms-in-machine-learning/)

3. Maze Generation and Pathfinding
   - [Recursive Backtracking Maze Generation Algorithm](https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/)
   - [Perfect Maze Generation using DFS](https://www.geeksforgeeks.org/maze-generation-algorithms/)

4. Visualization Framework
   - [Pygame Official Documentation](https://www.pygame.org/docs/)
   - [Pygame Drawing Reference](https://www.pygame.org/docs/ref/draw.html)
   - [Pygame Display Module](https://www.pygame.org/docs/ref/display.html)

## Testing Strategy

### Test Development
We leveraged generative AI (Claude) to help create comprehensive unit tests for our components.
- Covered edge cases
- Identified potential issues early

### Test Results
Our test suite helped identify and fix several issues:
- Pheromone accumulation bugs
- Movement errors
- Parameter boundary issues
- Visualization issues
