#Contains the core logic for different algorithms
"""
Pathfinding algorithms for maze solving
"""

import pygame
from collections import deque
import heapq
from constants import BACKGROUND


class PathfindingAlgorithm:
    """Base class for pathfinding algorithms"""
    
    def __init__(self, maze):
        self.maze = maze
    
    def solve(self, screen, offset_x, offset_y, cell_size, delay=10):
        """Solve the maze - to be implemented by subclasses"""
        raise NotImplementedError
    
    def _reconstruct_path(self, end_cell, parent):
        """Reconstruct the path from start to end"""
        current = end_cell
        while current:
            current.is_path = True
            current = parent[current]
    
    def _visualize(self, screen, offset_x, offset_y, cell_size):
        """Update the screen to show current progress"""
        screen.fill(BACKGROUND)
        self.maze.draw(screen, offset_x, offset_y, cell_size)
        pygame.display.flip()
    
    def _get_start_cell(self):
        """Get the start cell from maze"""
        return self.maze.grid[self.maze.start[0]][self.maze.start[1]]
    
    def _is_valid_start_end(self):
        """Check if start and end points are set"""
        return bool(self.maze.start and self.maze.end)


class BFS(PathfindingAlgorithm):
    """Breadth-First Search algorithm"""
    
    def solve(self, screen, offset_x, offset_y, cell_size, delay=10):
        """Find path using BFS"""
        if not self._is_valid_start_end():
            return False
        
        self.maze.clear_path()
        queue = deque()
        start_cell = self._get_start_cell()
        queue.append(start_cell)
        parent = {start_cell: None}
        
        while queue:
            current = queue.popleft()
            
            if (current.row, current.col) == self.maze.end:
                self._reconstruct_path(current, parent)
                return True
            
            current.is_visited_search = True
            
            if delay > 0:
                self._visualize(screen, offset_x, offset_y, cell_size)
                pygame.time.delay(delay)
            
            for neighbor in self.maze.get_neighbors_pathfinding(current):
                if neighbor not in parent:
                    parent[neighbor] = current
                    queue.append(neighbor)
        
        return False
    
class DFS(PathfindingAlgorithm):
    """Depth-First Search algorithm"""
    
    def solve(self, screen, offset_x, offset_y, cell_size, delay=10):
        """Find path using DFS"""
        if not self._is_valid_start_end():
            return False
        
        self.maze.clear_path()
        stack = [self._get_start_cell()]
        parent = {stack[0]: None}
        
        while stack:
            current = stack.pop()
            
            if (current.row, current.col) == self.maze.end:
                self._reconstruct_path(current, parent)
                return True
            
            if not current.is_visited_search:
                current.is_visited_search = True
                
                if delay > 0:
                    self._visualize(screen, offset_x, offset_y, cell_size)
                    pygame.time.delay(delay)
                
                for neighbor in self.maze.get_neighbors_pathfinding(current):
                    if neighbor not in parent:
                        parent[neighbor] = current
                        stack.append(neighbor)
        
        return False


class AStar(PathfindingAlgorithm):
    """A* Search algorithm with Manhattan distance heuristic"""
    
    def solve(self, screen, offset_x, offset_y, cell_size, delay=10):
        """Find path using A*"""
        if not self._is_valid_start_end():
            return False
        
        self.maze.clear_path()
        
        def heuristic(cell):
            """Manhattan distance heuristic"""
            return abs(cell.row - self.maze.end[0]) + abs(cell.col - self.maze.end[1])
        
        start_cell = self._get_start_cell()
        open_set = [(0, id(start_cell), start_cell)]
        parent = {start_cell: None}
        g_score = {start_cell: 0}
        
        while open_set:
            _, _, current = heapq.heappop(open_set)
            
            if (current.row, current.col) == self.maze.end:
                self._reconstruct_path(current, parent)
                return True
            
            current.is_visited_search = True
            
            if delay > 0:
                self._visualize(screen, offset_x, offset_y, cell_size)
                pygame.time.delay(delay)
            
            for neighbor in self.maze.get_neighbors_pathfinding(current):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor)
                    heapq.heappush(open_set, (f_score, id(neighbor), neighbor))
        
        return False
