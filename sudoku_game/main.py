"""
Sudoku Solver Visualizer using DFS with Backtracking
"""

import pygame
import time
from constants import *
from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
from sudoku_visualizer import SudokuVisualizer
from puzzles import PUZZLES


class SudokuApp:
    """Main Sudoku application"""
    
    def __init__(self):
        """Initialize the application"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku Solver - DFS Visualization")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.solving = False
        
        # Start with easy puzzle
        self.load_puzzle('easy')
    
    def load_puzzle(self, difficulty='easy'):
        """Load a new puzzle"""
        puzzle = PUZZLES.get(difficulty, PUZZLES['easy'])
        self.board = SudokuBoard(puzzle)
        self.visualizer = SudokuVisualizer(self.screen, self.board)
        self.solver = SudokuSolver(self.board, self.visualizer)
        self.visualizer.draw()
    
    def solve_puzzle(self):
        """Solve the current puzzle with visualization"""
        if not self.solving:
            self.solving = True
            success = self.solver.solve(animate=True)
            
            if success:
                stats = self.solver.get_stats()
                print(f"✓ Puzzle solved!")
                print(f"  Steps: {stats['steps']}")
                print(f"  Backtracks: {stats['backtracks']}")
            else:
                print("✗ Solving interrupted or no solution found")
            
            self.solving = False
    
    def handle_events(self):
        """Handle user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                elif event.key == pygame.K_SPACE and not self.solving:
                    self.solve_puzzle()
                
                elif event.key == pygame.K_1 and not self.solving:
                    print("\n📋 Loading Easy puzzle...")
                    self.load_puzzle('easy')
                
                elif event.key == pygame.K_2 and not self.solving:
                    print("\n📋 Loading Medium puzzle...")
                    self.load_puzzle('medium')
                
                elif event.key == pygame.K_3 and not self.solving:
                    print("\n📋 Loading Hard puzzle...")
                    self.load_puzzle('hard')
                
                elif event.key == pygame.K_d and not self.solving:
                    print("\n📋 Loading Demo puzzle...")
                    self.load_puzzle('demo')
    
    def run(self):
        """Main application loop"""
        print("🧩 Sudoku Solver - DFS with Backtracking")
        print("=" * 50)
        print("\nControls:")
        print("  SPACE - Solve puzzle")
        print("  1 - Easy puzzle")
        print("  2 - Medium puzzle")
        print("  3 - Hard puzzle")
        print("  D - Demo puzzle")
        print("  ESC - Quit")
        print("\nWatch the algorithm explore and backtrack!")
        print("=" * 50)
        
        while self.running:
            self.handle_events()
            self.clock.tick(60)
        
        pygame.quit()


if __name__ == "__main__":
    app = SudokuApp()
    app.run()