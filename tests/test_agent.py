import unittest
import numpy as np
from agents.agent import Agent

class TestAgent(unittest.TestCase):
    def setUp(self):
        """Create a simple maze and some agents for testing."""
        # create 5x5 maze (all paths, no walls)
        self.maze = np.zeros((5, 5))
        
        # create test agent at center
        self.agent = Agent(2, 2, 4, 4)  # start at (2,2), goal at (4,4)
        
    def test_initialization(self):
        """Test agent initialization."""
        self.assertEqual(self.agent.x, 2)
        self.assertEqual(self.agent.y, 2)
        self.assertEqual(self.agent.goal_x, 4)
        self.assertEqual(self.agent.goal_y, 4)
        self.assertEqual(self.agent.vx, 0)
        self.assertEqual(self.agent.vy, 0)
        
    def test_goal_seeking(self):
        """Test that agent moves toward goal."""
        dx, dy = self.agent._goal_seeking()
        # should move toward (4,4) from (2,2)
        self.assertGreater(dx, 0)  # should move right
        self.assertGreater(dy, 0)  # should move down
        
    def test_separation(self):
        """Test that agent maintains distance from others."""
        # create another agent very close
        other_agent = Agent(2, 3, 4, 4)  # right next to test agent
        
        dx, dy = self.agent._separation([other_agent])
        self.assertEqual(dx, 0)  # no horizontal separation needed
        self.assertLess(dy, 0)  # should move away vertically
        
    def test_wall_collision(self):
        """Test that agent doesn't move through walls."""
        # create a larger maze to ensure wall is within bounds
        self.maze = np.zeros((7, 7))  # increased size
        
        # place agent and wall
        self.agent.x = 3  # move agent to center
        self.agent.y = 3
        self.maze[3, 4] = 1  # wall to the right of agent
        
        # try to move right
        self.agent.vx = 1
        self.agent.vy = 0
        original_x = self.agent.x
        
        self.agent.move(self.maze, [])
        
        # should not have moved
        self.assertEqual(self.agent.x, original_x)
        
    def test_movement_normalization(self):
        """Test that velocity is normalized."""
        # create large velocities
        self.agent.vx = 5
        self.agent.vy = 5
        
        self.agent.move(self.maze, [])
        
        # velocity should be normalized (magnitude = 1)
        magnitude = np.sqrt(self.agent.vx**2 + self.agent.vy**2)
        self.assertAlmostEqual(magnitude, 1.0)

    def test_weighted_behaviors(self):
        """Test that behavior weights affect movement appropriately"""
        # Create a test scenario with multiple agents
        other_agent = Agent(2, 2.5, 4, 4)  # Very close to test agent
        test_agent = Agent(2, 2, 4, 4)
        
        # Set strong separation weight
        test_agent.swarm_behavior.set_weights(separation=3.0)  # Increased from 2.0 to 3.0
        
        # Get movement vector
        test_agent.move(self.maze, [other_agent])
        
        # Should move strongly away from other agent
        self.assertLess(test_agent.vy, -0.5)  # Move up away from other agent

    def test_pathfinding_empty_maze(self):
        """Test pathfinding in an empty maze."""
        # Create empty 5x5 maze
        maze = np.zeros((5, 5))
        
        # Agent at (0,0) trying to reach (4,4)
        agent = Agent(0, 0, 4, 4)
        agent.update_path(maze)
        
        # Should find a path
        self.assertGreater(len(agent.current_path), 0)
        # Path should start at agent position
        self.assertEqual(agent.current_path[0], (0, 0))
        # Path should end at goal
        self.assertEqual(agent.current_path[-1], (4, 4))
        
    def test_pathfinding_with_walls(self):
        """Test pathfinding with walls blocking direct path."""
        # Create maze with wall
        maze = np.zeros((5, 5))
        maze[2, :3] = 1  # Horizontal wall in middle
        
        # Agent needs to go around wall
        agent = Agent(0, 0, 0, 4)
        agent.update_path(maze)
        
        # Should find a path
        self.assertGreater(len(agent.current_path), 0)
        # Path should avoid walls
        for x, y in agent.current_path:
            self.assertEqual(maze[y, x], 0)
            
    def test_pathfinding_no_path(self):
        """Test handling when no path exists."""
        # Create maze with blocking wall
        maze = np.zeros((5, 5))
        maze[2, :] = 1  # Complete horizontal wall
        
        # Agent can't reach goal
        agent = Agent(0, 0, 0, 4)
        agent.update_path(maze)
        
        # Should return empty path
        self.assertEqual(len(agent.current_path), 0)
        
    def test_pathfinding_shortest_path(self):
        """Test that pathfinder finds optimal path."""
        # Create empty maze
        maze = np.zeros((3, 3))
        
        # Agent moving from corner to corner
        agent = Agent(0, 0, 2, 2)
        agent.update_path(maze)
        
        # Optimal path length should be 4 (including start and end)
        # (0,0) -> (1,1) -> (2,2)
        self.assertEqual(len(agent.current_path), 3)

if __name__ == '__main__':
    unittest.main() 