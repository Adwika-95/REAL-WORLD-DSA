#manages the visualization of algorithm steps 
"""
Algorithm Visualizer - Modern UI for Breadth-First Search visualization
"""
import pygame
import sys
import time
from constants import *
from ui_components import  Button, Label, Dropdown
from maze import Maze
from algorithms import BFS, AStar, DFS

class UIRenderer:
    """Handles rendering of UI elements and visualization"""

    LEGEND_LINE_HEIGHT = 35
    CIRCLE_RADIUS = 10
    LEGEND_PADDING = 40
    
    def __init__(self, screen, font, small_font, title_font, info_font, maze_offset_x, maze_offset_y):
        self.screen = screen
        self.font = font
        self.small_font = small_font
        self.title_font = title_font
        self.info_font = info_font
        self.maze_offset_x = maze_offset_x
        self.maze_offset_y = maze_offset_y
    
    def draw_title(self):
        """Draw the title with modern styling"""
        # Draw title background panel
        panel_height = 70
        pygame.draw.rect(self.screen, PANEL_BG, (0, 0, WINDOW_WIDTH, panel_height))
        pygame.draw.rect(self.screen, ACCENT_COLOR, (0, panel_height - 3, WINDOW_WIDTH, 3))
        
        # Main title
        title = self.title_font.render("ALGORITHM VISUALIZER", True, DARK_GRAY)
        subtitle_font = pygame.font.Font(None, 22)
        subtitle = subtitle_font.render("Pathfinding algorithms", True, GRAY)
        
        # Center the titles
        title_x = WINDOW_WIDTH // 2 - title.get_width() // 2
        subtitle_x = WINDOW_WIDTH // 2 - subtitle.get_width() // 2
        
        self.screen.blit(title, (title_x, 12))
        self.screen.blit(subtitle, (subtitle_x, 45))
    
    def draw_maze_border(self):
        """Draw modern border around the maze"""
        maze_width = MAZE_COLS * CELL_SIZE
        maze_height = MAZE_ROWS * CELL_SIZE
        border_padding = 8
        
        # Outer shadow effect
        shadow_offset = 3
        pygame.draw.rect(
            self.screen, (180, 180, 180),
            (self.maze_offset_x - border_padding + shadow_offset, 
             self.maze_offset_y - border_padding + shadow_offset,
             maze_width + 2 * border_padding, maze_height + 2 * border_padding),
            border_radius=8
        )
        
        # Main border
        pygame.draw.rect(
            self.screen, PANEL_BG,
            (self.maze_offset_x - border_padding, self.maze_offset_y - border_padding,
             maze_width + 2 * border_padding, maze_height + 2 * border_padding),
            border_radius=8
        )
        
        pygame.draw.rect(
            self.screen, MAZE_BORDER,
            (self.maze_offset_x - border_padding, self.maze_offset_y - border_padding,
             maze_width + 2 * border_padding, maze_height + 2 * border_padding),
            4, border_radius=8
        )
    
    def draw_legend(self):
        """Draw the modern legend panel on the right side"""
        maze_width = MAZE_COLS * CELL_SIZE
        legend_x = self.maze_offset_x + maze_width + self.LEGEND_PADDING
        legend_y = self.maze_offset_y + 20
        
        # Legend panel background with more padding
        panel_width = 200
        panel_height = 280
        panel_padding = 20
        pygame.draw.rect(self.screen, PANEL_BG, 
                        (legend_x - panel_padding, legend_y - panel_padding, panel_width, panel_height),
                        border_radius=10)
        pygame.draw.rect(self.screen, ACCENT_COLOR, 
                        (legend_x - panel_padding, legend_y - panel_padding, panel_width, panel_height),
                        3, border_radius=10)
        
        # Legend title with more padding
        title_font = pygame.font.Font(None, 26)
        title = title_font.render("Legend", True, DARK_GRAY)
        self.screen.blit(title, (legend_x + 10, legend_y + 5))
        
        # Divider line with padding
        pygame.draw.line(self.screen, LIGHT_GRAY, 
                        (legend_x + 10, legend_y + 32), 
                        (legend_x + 160, legend_y + 32), 2)
        
        legend_y += 48
        
        # Draw legend items with circles
        legend_items = [
            ("Start Point", GREEN),
            ("End Point", RED),
            ("Exploring", EXPLORING_COLOR),
            ("Visited", VISITED_COLOR),
            ("Final Path", YELLOW),
            ("Wall", WALL_COLOR),
        ]
        
        for i, (label, color) in enumerate(legend_items):
            y = legend_y + i * self.LEGEND_LINE_HEIGHT
            
            # Draw colored indicator with more spacing
            if label == "Wall":
                # Square for walls
                pygame.draw.rect(self.screen, color, 
                               (legend_x + 15, y + 3, 16, 16), border_radius=3)
            else:
                # Circle for other items
                pygame.draw.circle(self.screen, color, 
                                 (legend_x + 23, y + 11), self.CIRCLE_RADIUS)
                pygame.draw.circle(self.screen, DARK_GRAY, 
                                 (legend_x + 23, y + 11), self.CIRCLE_RADIUS, 2)
            
            # Draw label with more spacing
            text = self.small_font.render(label, True, DARK_GRAY)
            self.screen.blit(text, (legend_x + 50, y + 3))
    
    def draw_statistics(self, solve_time, nodes_visited, path_length, algorithm_name=None):
        """Draw the modern statistics panel below the maze"""
        if solve_time <= 0:
            return
        
        # Position below maze with more spacing
        maze_height = MAZE_ROWS * CELL_SIZE
        stats_y = self.maze_offset_y + maze_height + 35
        stats_x = self.maze_offset_x
        
        box_width = MAZE_COLS * CELL_SIZE
        box_height = 95
        
        # Panel background with shadow
        shadow_offset = 3
        pygame.draw.rect(self.screen, (180, 180, 180),
                        (stats_x + shadow_offset, stats_y + shadow_offset, 
                         box_width, box_height), border_radius=10)
        
        pygame.draw.rect(self.screen, PANEL_BG, 
                        (stats_x, stats_y, box_width, box_height), border_radius=10)
        pygame.draw.rect(self.screen, BUTTON_SUCCESS, 
                        (stats_x, stats_y, box_width, box_height), 3, border_radius=10)
        
        # Title with more padding - show algorithm name
        title_font = pygame.font.Font(None, 26)
        title_text = f"{algorithm_name} Statistics" if algorithm_name else "Statistics"
        title = title_font.render(title_text, True, DARK_GRAY)
        self.screen.blit(title, (stats_x + 30, stats_y + 18))
        
        # Stats in horizontal layout
        stats = [
            ("Time:", f"{solve_time:.3f}s"),
            ("Nodes Visited:", f"{nodes_visited}"),
            ("Path Length:", f"{path_length}"),
        ]
        
        stat_font = pygame.font.Font(None, 20)
        value_font = pygame.font.Font(None, 24)
        
        # Calculate spacing for horizontal layout with more padding
        stat_spacing = box_width // 3
        start_x = stats_x + 50
        y = stats_y + 43
        
        for i, (label, value) in enumerate(stats):
            x = start_x + i * stat_spacing
            label_surf = stat_font.render(label, True, GRAY)
            value_surf = value_font.render(value, True, DARK_GRAY)
            self.screen.blit(label_surf, (x, y))
            self.screen.blit(value_surf, (x, y + 24))


class MazeVisualizer:
    """Main application for the maze solver visualizer"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        
        # Fonts - Modern sizing
        self.font = pygame.font.Font(None, 26)
        self.small_font = pygame.font.Font(None, 22)
        self.title_font = pygame.font.Font(None, 44)
        self.info_font = pygame.font.Font(None, 20)
        self.button_font = pygame.font.Font(None, 24)  # Dedicated font for buttons
        
        # Create maze
        self.maze = Maze(MAZE_ROWS, MAZE_COLS)
        self.mode = "placing_start"
        
        # Calculate maze position - centered with more space
        self.maze_offset_x = 40
        self.maze_offset_y = 110
        
        # Create algorithms
        self.algorithms = {
            "BFS Algorithm": BFS(self.maze),
            "DFS Algorithm": DFS(self.maze),
            "A Star Algorithm": AStar(self.maze)
        }
        
        # Statistics
        self.solve_time = 0
        self.nodes_visited = 0
        self.path_length = 0
        self.current_algorithm = None
        
        # UI elements
        self._init_ui()
        
        # State
        self.running = True
        self.solving = False
        
        # Renderer
        self.renderer = UIRenderer(
            self.screen, self.font, self.small_font, self.title_font, 
            self.info_font, self.maze_offset_x, self.maze_offset_y
        )
        
    def _init_ui(self):
        """Initialize all UI components with side layout"""
        # Buttons on the right side - moved lower
        maze_width = MAZE_COLS * CELL_SIZE
        button_x = self.maze_offset_x + maze_width + 40
        button_start_y = self.maze_offset_y + 400  # Moved down from 280 to 400
        button_width = 200
        button_height = 50
        button_spacing = 15
        
        # Stack buttons vertically on the right
        self.generate_button = Button(button_x, button_start_y, 
                                      button_width, button_height, "Generate", BUTTON_PRIMARY)
        
        # Single solve button
        self.solve_button = Button(button_x, button_start_y + button_height + button_spacing, 
                                   button_width, button_height, "Solve", BUTTON_SUCCESS)
        
        self.reset_button = Button(button_x, button_start_y + 2 * (button_height + button_spacing), 
                                   button_width, button_height, "Reset All", BUTTON_WARNING)
        self.clear_button = Button(button_x, button_start_y + 3 * (button_height + button_spacing), 
                                   button_width, button_height, "Clear Path", BUTTON_DANGER)
        
        # Algorithm selection label and dropdown (below all buttons)
        dropdown_y = button_start_y - 60
        self.algorithm_label = Label(button_x, dropdown_y - 35, "Select Algorithm:", self.small_font, DARK_GRAY)
        self.algorithm_dropdown = Dropdown(
            button_x, dropdown_y, button_width, button_height,
            ["BFS Algorithm", "DFS Algorithm", "A Star Algorithm"],
            self.font
        )

        # Status label with better positioning
        self.status_label = Label(40, 78, "", self.small_font, DARK_GRAY)
        
    def handle_events(self):
        """Handle all pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEMOTION:
                self._handle_hover(pygame.mouse.get_pos())
    
    def _handle_click(self, pos):
        """Handle mouse click events"""
        # Handle dropdown first (it needs priority for expanded state)
        if self.algorithm_dropdown.handle_click(pos):
            return
        
        if self.generate_button.is_clicked(pos):
            self._generate_maze()
        elif self.solve_button.is_clicked(pos) and not self.solving:
            selected_algorithm = self.algorithm_dropdown.options[self.algorithm_dropdown.selected]
            self._solve_maze(selected_algorithm)
        elif self.reset_button.is_clicked(pos):
            self._reset_visualization()
        elif self.clear_button.is_clicked(pos):
            self._clear_path()
        else:
            self._handle_maze_click(pos)
    
    def _handle_hover(self, pos):
        """Handle mouse hover events"""
        self.algorithm_dropdown.update_hover(pos)
        self.generate_button.update_hover(pos)
        self.solve_button.update_hover(pos)
        self.reset_button.update_hover(pos)
        self.clear_button.update_hover(pos)
    
    def _generate_maze(self):
        """Generate a new maze"""
        self.maze.generate_maze()
        self.maze.start = None
        self.maze.end = None
        self.mode = "placing_start"
        self.solving = False
    
    def _solve_maze(self, algorithm_name="BFS Algorithm"):
        """Solve the maze using selected algorithm"""
        if not self.maze.start or not self.maze.end:
            return
        
        self.solving = True
        self.current_algorithm = algorithm_name
        algorithm = self.algorithms[algorithm_name]
        
        start_time = time.time()
        algorithm.solve(
            self.screen, self.maze_offset_x, self.maze_offset_y,
            CELL_SIZE, VISUALIZATION_DELAY
        )
        
        self.solve_time = time.time() - start_time
        self.nodes_visited = sum(1 for row in self.maze.grid for cell in row if cell.is_visited_search)
        self.path_length = sum(1 for row in self.maze.grid for cell in row if cell.is_path)
        self.solving = False
    
    def _clear_path(self):
        """Clear only the pathfinding visualization, keep maze structure"""
        self.maze.clear_path()
        self.solve_time = 0
        self.nodes_visited = 0
        self.path_length = 0
        self.current_algorithm = None
        self.solving = False
    
    def _reset_visualization(self):
        """Reset everything including maze structure"""
        self.maze.clear_path()
        self.maze.start = None
        self.maze.end = None
        self.mode = "placing_start"
        self.solve_time = 0
        self.nodes_visited = 0
        self.path_length = 0
        self.solving = False
    
    def _handle_maze_click(self, pos):
        """Handle clicks on the maze grid"""
        mx, my = pos
        
        # Check if click is within maze bounds
        maze_right = self.maze_offset_x + MAZE_COLS * CELL_SIZE
        maze_bottom = self.maze_offset_y + MAZE_ROWS * CELL_SIZE
        
        if not (self.maze_offset_x <= mx < maze_right and self.maze_offset_y <= my < maze_bottom):
            return
        
        # Calculate cell coordinates
        col = (mx - self.maze_offset_x) // CELL_SIZE
        row = (my - self.maze_offset_y) // CELL_SIZE
        
        # Place start or end point based on mode
        if self.mode == "placing_start":
            self.maze.start = (row, col)
            self.mode = "placing_end"
        elif self.mode == "placing_end":
            if (row, col) != self.maze.start:
                self.maze.end = (row, col)
                self.mode = "ready"
        elif self.mode == "ready":
            # Allow re-placing points
            if self.maze.start and (row, col) == self.maze.start:
                self.maze.start = None
                self.mode = "placing_start"
            elif self.maze.end and (row, col) == self.maze.end:
                self.maze.end = None
                self.mode = "placing_end"
    
    def _update_status_message(self):
        """Update the status message based on current mode"""
        messages = {
            "placing_start": ">> Click on the maze to place the START point (Green circle)",
            "placing_end": ">> Click on the maze to place the END point (Red circle)",
            "ready": ">> Ready! Click 'Solve BFS' to visualize the pathfinding algorithm"
        }
        self.status_label.update_text(messages.get(self.mode, ""))
    
    def draw(self):
        """Draw all elements on screen with modern styling"""
        self.screen.fill(BACKGROUND)
        
        # Draw title panel
        self.renderer.draw_title()
        
        # Update and draw status
        self._update_status_message()
        self.status_label.draw(self.screen)
        
        # Draw maze with border
        self.renderer.draw_maze_border()
        self.maze.draw(self.screen, self.maze_offset_x, self.maze_offset_y, CELL_SIZE)
        
        # Draw legend and statistics
        self.renderer.draw_legend()
        self.renderer.draw_statistics(self.solve_time, self.nodes_visited, self.path_length, self.current_algorithm)
        
        # Draw control buttons with button font
        self.generate_button.draw(self.screen, self.button_font)
        self.solve_button.draw(self.screen, self.button_font)
        self.reset_button.draw(self.screen, self.button_font)
        self.clear_button.draw(self.screen, self.button_font)
        
        # Draw algorithm selection label and dropdown
        self.algorithm_label.draw(self.screen)
        self.algorithm_dropdown.draw(self.screen)
        
        # Draw expanded dropdown options on top of everything
        self.algorithm_dropdown.draw_expanded_options(self.screen)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        self.maze.generate_maze()
        
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()