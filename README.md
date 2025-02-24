# Dynamic Maze Solver with Swarm Intelligence
---
## Description
A dynamic maze generation and solving system that implements swarm intelligence, specifically Ant Colony Optimization (ACO), to reach a goal in the maze.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/trevritchie/dynamic-maze-aco.git 
   ```

2. Navigate to the project directory:
    ```sh
    cd dynamic-maze-solver
    ```
    
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the main simulation:
   ```sh
   python main.py
   ```

## Features
- Dynamic maze generation with real-time updates
- Ant Colony Optimization (ACO) pathfinding implementation
- Visual maze rendering with path visualization

## Technologies Used
- Python
- Pygame for visualization
- NumPy for efficient matrix operations
- Custom ACO implementation

## Project Structure
```
├── __init__.py
├── main.py                 # Entry point and simulation controller
├── maze/
│   ├── __init__.py
│   ├── perfect_maze.py     # Perfect maze generation algorithms
│   └── dynamic_maze.py     # Handles runtime maze modifications
├── agents/
│   ├── __init__.py
│   ├── agent.py           # Base agent class
│   └── aco.py             # Ant Colony Optimization implementation
├── visualization/
│   ├── __init__.py
│   └── maze_renderer.py   # Pygame-based maze visualization
├── tests/
│   └── test_*.py         # Unit tests for each component
├── requirements.txt
└── README.md
```

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

Please ensure your code follows our style guidelines and includes appropriate tests.

## License
This project is licensed under the MIT License.

## Contact
Carter Quattlebaum, Donovan Saldarriaga, Trevor Ritchie

- GitHub:
   - [@Q-Cumbersome](https://github.com/Q-Cumbersome)
   - [@donovanSaladressing](https://github.com/donovanSaladressing)
   - [@trevritchie](https://github.com/trevritchie)
- Email: 
  - [quattlebaumcl@g.cofc.edu](mailto:quattlebaumcl@g.cofc.edu)
  - [saldarriagadv@g.cofc.edu](mailto:saldarriagadv@g.cofc.edu)
  - [ritchiets@g.cofc.edu](mailto:ritchiets@g.cofc.edu)

Project Link: [https://github.com/trevritchie/dynamic-maze-aco](https://github.com/trevritchie/dynamic-maze-aco)
