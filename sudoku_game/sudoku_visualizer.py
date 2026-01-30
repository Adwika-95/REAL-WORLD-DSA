"""
Visualization for Sudoku solving process
"""

import pygame
from constants import *


class SudokuVisualizer:
    """Handles visual rendering of Sudoku solving"""
    
    def __init__(self, screen, board):
        """Initialize visualizer"""
        self.screen = screen
        self.board = board
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.small_font = pygame.font.Font(None, SMALL_FONT_SIZE)
        self.title_font = pygame.font.Font(None, 32)
        self.is_complete = False
        
    def draw(self, current_cell=None, trying_value=None, backtracking=False, 
             steps=0, backtracks=0):
        """Draw the current board state"""
        self.screen.fill(WHITE)
        
        # Draw title
        title = self.title_font.render("Sudoku Solver - DFS with Backtracking", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))
        
        # Draw grid and numbers
        self._draw_grid()
        self._draw_numbers(current_cell, trying_value, backtracking)
        
        # Draw statistics
        self._draw_stats(steps, backtracks)
        
        # Draw instructions
        self._draw_instructions()
        
        pygame.display.flip()
    
    def _draw_grid(self):
        """Draw the Sudoku grid"""
        # Draw cells
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * CELL_SIZE
                y = 50 + row * CELL_SIZE
                
                # Highlight 3x3 boxes
                if (row // 3 + col // 3) % 2 == 0:
                    pygame.draw.rect(self.screen, (245, 245, 245), 
                                   (x, y, CELL_SIZE, CELL_SIZE))
        
        # Draw grid lines
        for i in range(GRID_SIZE + 1):
            thickness = 3 if i % 3 == 0 else 1
            
            # Horizontal lines
            pygame.draw.line(self.screen, BLACK,
                           (0, 50 + i * CELL_SIZE),
                           (WIDTH, 50 + i * CELL_SIZE), thickness)
            
            # Vertical lines
            pygame.draw.line(self.screen, BLACK,
                           (i * CELL_SIZE, 50),
                           (i * CELL_SIZE, 50 + WIDTH), thickness)
    
    def _draw_numbers(self, current_cell=None, trying_value=None, backtracking=False):
        """Draw the numbers on the board"""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = self.board.get_value(row, col)
                
                x = col * CELL_SIZE + CELL_SIZE // 2
                y = 50 + row * CELL_SIZE + CELL_SIZE // 2
                
                # Highlight current cell
                if current_cell and (row, col) == current_cell:
                    rect = pygame.Rect(col * CELL_SIZE + 2, 50 + row * CELL_SIZE + 2,
                                      CELL_SIZE - 4, CELL_SIZE - 4)
                    color = ERROR_COLOR if backtracking else SOLVING_COLOR
                    if self.is_complete:
                        color = SOLVED_COLOR
                    pygame.draw.rect(self.screen, color, rect)
                
                # Draw number
                if value != 0:
                    # Choose color based on whether it's fixed or being tried
                    if self.board.is_fixed(row, col):
                        color = FIXED_COLOR
                    elif current_cell and (row, col) == current_cell and trying_value:
                        color = BLACK
                    else:
                        color = GRAY
                    
                    text = self.font.render(str(value), True, color)
                    text_rect = text.get_rect(center=(x, y))
                    self.screen.blit(text, text_rect)
    
    def _draw_stats(self, steps, backtracks):
        """Draw solving statistics"""
        y_pos = 50 + WIDTH + 10
        
        stats_text = f"Steps: {steps}  |  Backtracks: {backtracks}"
        text = self.small_font.render(stats_text, True, BLACK)
        self.screen.blit(text, (10, y_pos))
    
    def _draw_instructions(self):
        """Draw instructions"""
        y_pos = HEIGHT - 40
        
        if self.is_complete:
            text = "Puzzle Solved! Press SPACE for new puzzle or ESC to quit"
        else:
            text = "Press SPACE to solve | ESC to quit"
        
        instruction = self.small_font.render(text, True, GRAY)
        self.screen.blit(instruction, (WIDTH // 2 - instruction.get_width() // 2, y_pos))
    
    def mark_complete(self):
        """Mark the puzzle as complete"""
        self.is_complete = True
        self.draw()