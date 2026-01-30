"""
Sudoku board management and validation
"""


class SudokuBoard:
    """Represents a Sudoku board with validation"""
    
    def __init__(self, puzzle):
        """Initialize with a puzzle (0 represents empty cells)"""
        self.board = [row[:] for row in puzzle]  # Deep copy
        self.original = [row[:] for row in puzzle]  # Track fixed cells
        self.size = 9
        
    def is_valid_move(self, row, col, num):
        """Check if placing num at (row, col) is valid"""
        # Check row
        if num in self.board[row]:
            return False
        
        # Check column
        if num in [self.board[r][col] for r in range(self.size)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.board[r][c] == num:
                    return False
        
        return True
    
    def find_empty(self):
        """Find the next empty cell (returns row, col or None)"""
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return row, col
        return None
    
    def is_fixed(self, row, col):
        """Check if a cell is part of the original puzzle"""
        return self.original[row][col] != 0
    
    def get_value(self, row, col):
        """Get the value at a cell"""
        return self.board[row][col]
    
    def set_value(self, row, col, value):
        """Set the value at a cell"""
        self.board[row][col] = value
    
    def is_complete(self):
        """Check if the board is completely filled"""
        return all(self.board[row][col] != 0 
                  for row in range(self.size) 
                  for col in range(self.size))