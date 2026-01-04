#handles maze generation and manipulation 
"""
Maze generation and rendering with modern styling
"""

import pygame
import random
from constants import (WALL_COLOR, PATH_BG, YELLOW, VISITED_COLOR, 
                      GREEN, RED, WHITE, DARK_GRAY, EXPLORING_COLOR)

class MazeCell:
    """Represents a single cell in the maze"""
    
    # Direction mappings
    DIRECTIONS = {
        'up': (-1, 0, 'top', 'bottom'),
        'down': (1, 0, 'bottom', 'top'),
        'left': (0, -1, 'left', 'right'),
        'right': (0, 1, 'right', 'left'),
    }
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.is_path = False
        self.is_visited_search = False
        
    def draw(self, screen, x, y, cell_size):
        """Draw the cell with its walls and state with modern colors"""
        # Draw cell background based on state
        if self.is_path:
            # Final path - bright yellow
            pygame.draw.rect(screen, YELLOW, (x, y, cell_size, cell_size))
        elif self.is_visited_search:
            # Visited during search - light blue
            pygame.draw.rect(screen, VISITED_COLOR, (x, y, cell_size, cell_size))
        else:
            # Default white background
            pygame.draw.rect(screen, PATH_BG, (x, y, cell_size, cell_size))
        
        # Draw walls
        self._draw_walls(screen, x, y, cell_size)
    
    def _draw_walls(self, screen, x, y, cell_size):
        """Draw walls for this cell with modern styling"""
        wall_thickness = 3
        walls_coords = {
            'top': ((x, y), (x + cell_size, y)),
            'right': ((x + cell_size, y), (x + cell_size, y + cell_size)),
            'bottom': ((x, y + cell_size), (x + cell_size, y + cell_size)),
            'left': ((x, y), (x, y + cell_size)),
        }
        
        for direction, (start, end) in walls_coords.items():
            if self.walls[direction]:
                pygame.draw.line(screen, WALL_COLOR, start, end, wall_thickness)


class Maze:
    """Manages the maze grid, generation, and rendering"""
    
    # Direction deltas for neighbor checking
    NEIGHBOR_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[MazeCell(r, c) for c in range(cols)] for r in range(rows)]
        self.start = None
        self.end = None
        
    def generate_maze(self):
        """Generate a maze using recursive backtracking algorithm"""
        self._reset_maze()
        self._recursive_backtrack()
    
    def _reset_maze(self):
        """Reset all cells to initial state"""
        for row in self.grid:
            for cell in row:
                cell.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
                cell.visited = False
                cell.is_path = False
                cell.is_visited_search = False
    
    def _recursive_backtrack(self):
        """Generate maze using recursive backtracking algorithm"""
        stack = []
        current = self.grid[0][0]
        current.visited = True
        stack.append(current)
        
        while stack:
            current = stack[-1]
            neighbors = self._get_unvisited_neighbors(current)
            
            if neighbors:
                next_cell = random.choice(neighbors)
                self._remove_wall(current, next_cell)
                next_cell.visited = True
                stack.append(next_cell)
            else:
                stack.pop()
        
        # Reset visited flags for pathfinding
        self._reset_visited_flags()
    
    def _reset_visited_flags(self):
        """Reset visited flags after maze generation"""
        for row in self.grid:
            for cell in row:
                cell.visited = False
    
    def _get_unvisited_neighbors(self, cell):
        """Get unvisited neighboring cells"""
        neighbors = []
        
        for dr, dc in self.NEIGHBOR_DIRECTIONS:
            new_row, new_col = cell.row + dr, cell.col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                neighbor = self.grid[new_row][new_col]
                if not neighbor.visited:
                    neighbors.append(neighbor)
        
        return neighbors
    
    def _remove_wall(self, cell1, cell2):
        """Remove wall between two adjacent cells"""
        dr = cell2.row - cell1.row
        dc = cell2.col - cell1.col
        
        wall_map = {
            (1, 0): ('bottom', 'top'),
            (-1, 0): ('top', 'bottom'),
            (0, 1): ('right', 'left'),
            (0, -1): ('left', 'right'),
        }
        
        if (dr, dc) in wall_map:
            wall1, wall2 = wall_map[(dr, dc)]
            cell1.walls[wall1] = False
            cell2.walls[wall2] = False
    
    def get_neighbors_pathfinding(self, cell):
        """Get accessible neighboring cells for pathfinding"""
        neighbors = []
        
        # Check top
        if not cell.walls['top'] and cell.row > 0:
            neighbors.append(self.grid[cell.row - 1][cell.col])
        # Check bottom
        if not cell.walls['bottom'] and cell.row < self.rows - 1:
            neighbors.append(self.grid[cell.row + 1][cell.col])
        # Check left
        if not cell.walls['left'] and cell.col > 0:
            neighbors.append(self.grid[cell.row][cell.col - 1])
        # Check right
        if not cell.walls['right'] and cell.col < self.cols - 1:
            neighbors.append(self.grid[cell.row][cell.col + 1])
        
        return neighbors
    
    def draw(self, screen, offset_x, offset_y, cell_size):
        """Draw the entire maze"""
        for row in self.grid:
            for cell in row:
                x = offset_x + cell.col * cell_size
                y = offset_y + cell.row * cell_size
                cell.draw(screen, x, y, cell_size)
        
        # Draw start point (green circle)
        if self.start:
            self._draw_marker(screen, self.start, offset_x, offset_y, cell_size, GREEN)
        
        # Draw end point (red circle)
        if self.end:
            self._draw_marker(screen, self.end, offset_x, offset_y, cell_size, RED)
    
    def _draw_marker(self, screen, position, offset_x, offset_y, cell_size, color):
        """Draw a modern marker (start or end point) on the maze"""
        x = offset_x + position[1] * cell_size + cell_size // 2
        y = offset_y + position[0] * cell_size + cell_size // 2
        radius = cell_size // 2 - 3
        
        # Draw outer glow effect
        glow_radius = radius + 4
        glow_color = (*color[:3], 50) if len(color) == 3 else color
        for i in range(3):
            alpha = 255 - (i * 80)
            current_radius = glow_radius + i * 2
            glow_surf = pygame.Surface((current_radius * 2, current_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*color, alpha // 3), 
                             (current_radius, current_radius), current_radius)
            screen.blit(glow_surf, (x - current_radius, y - current_radius))
        
        # Draw main circle
        pygame.draw.circle(screen, color, (x, y), radius)
        pygame.draw.circle(screen, WHITE, (x, y), radius, 2)
        
        # Draw inner highlight
        highlight_offset = radius // 3
        pygame.draw.circle(screen, (255, 255, 255, 100), 
                         (x - highlight_offset, y - highlight_offset), radius // 4)
    
    def clear_path(self):
        """Clear pathfinding visualization"""
        for row in self.grid:
            for cell in row:
                cell.is_path = False
                cell.is_visited_search = False
                cell.visited = False