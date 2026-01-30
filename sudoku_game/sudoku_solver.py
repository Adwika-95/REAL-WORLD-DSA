"""
DFS-based Sudoku solver with backtracking
"""

import time
import pygame
from constants import SOLVE_DELAY


class SudokuSolver:
    """Solves Sudoku using DFS with backtracking"""
    
    def __init__(self, board, visualizer=None):
        """Initialize solver with board and optional visualizer"""
        self.board = board
        self.visualizer = visualizer
        self.steps = 0
        self.backtrack_count = 0
        self.should_stop = False
        
    def solve(self, animate=True):
        """Solve the puzzle using DFS with backtracking"""
        self.steps = 0
        self.backtrack_count = 0
        self.should_stop = False
        
        result = self._solve_recursive(animate)
        
        if self.visualizer and result:
            self.visualizer.mark_complete()
        
        return result
    
    def _solve_recursive(self, animate=True):
        """Recursive DFS solver"""
        # Check for quit events
        if self._check_quit():
            return False
        
        # Find next empty cell
        empty = self.board.find_empty()
        if empty is None:
            return True  # Puzzle solved!
        
        row, col = empty
        self.steps += 1
        
        # Try numbers 1-9
        for num in range(1, 10):
            if self._check_quit():
                return False
            
            if self.board.is_valid_move(row, col, num):
                # Place number
                self.board.set_value(row, col, num)
                
                # Visualize
                if animate and self.visualizer:
                    self.visualizer.draw(
                        current_cell=(row, col),
                        trying_value=num,
                        steps=self.steps,
                        backtracks=self.backtrack_count
                    )
                    time.sleep(SOLVE_DELAY)
                
                # Recurse
                if self._solve_recursive(animate):
                    return True
                
                # Backtrack
                self.board.set_value(row, col, 0)
                self.backtrack_count += 1
                
                # Visualize backtracking
                if animate and self.visualizer:
                    self.visualizer.draw(
                        current_cell=(row, col),
                        backtracking=True,
                        steps=self.steps,
                        backtracks=self.backtrack_count
                    )
                    time.sleep(SOLVE_DELAY / 2)
        
        return False
    
    def _check_quit(self):
        """Check if user wants to quit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_stop = True
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.should_stop = True
                return True
        return False
    
    def get_stats(self):
        """Return solving statistics"""
        return {
            'steps': self.steps,
            'backtracks': self.backtrack_count
        }