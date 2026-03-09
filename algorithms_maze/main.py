#entry point that ties everything together
"""
AlgoMaze - Pathfinding Algorithm Visualizer
A pygame-based application for visualizing maze generation and pathfinding algorithms.
"""
from algorithms_maze.visualizer import MazeVisualizer

def main():
    """Main entry point for the application"""
    visualizer = MazeVisualizer()
    visualizer.run()

if __name__ == "__main__":
    main()