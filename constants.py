#Stores configuration values and constants 
"""
Constants for Algorithm Visualizer
"""

# Window dimensions
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
CONTROL_PANEL_HEIGHT = 120

# Maze dimensions
CELL_SIZE = 22
MAZE_ROWS = 25
MAZE_COLS = 38

# Modern Color Palette
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (128, 128, 128)
LIGHT_GRAY = (189, 195, 199)
DARK_GRAY = (44, 62, 80)

# BFS Visualization Colors
GREEN = (39, 174, 96)          # Start point
RED = (231, 76, 60)            # End point
BLUE = (52, 152, 219)          # BFS exploration color
YELLOW = (241, 196, 15)        # Path color
PURPLE = (155, 89, 182)        # Current node
ORANGE = (230, 126, 34)        # Queue visualization
CYAN = (26, 188, 156)          # Visited nodes

# UI Colors - Modern Dark/Light Theme
BUTTON_PRIMARY = (52, 152, 219)    # Bright Blue
BUTTON_SUCCESS = (46, 204, 113)    # Bright Green
BUTTON_WARNING = (230, 126, 34)    # Orange
BUTTON_DANGER = (231, 76, 60)      # Red
BUTTON_HOVER = (72, 172, 239)      # Light Blue
BUTTON_TEXT = (255, 255, 255)      # White text

DROPDOWN_BG = (52, 73, 94)         # Dark blue-gray
DROPDOWN_HOVER = (71, 92, 113)     # Lighter blue-gray
TEXT_COLOR = (255, 255, 255)       # White

BACKGROUND = (236, 240, 241)       # Light gray
PANEL_BG = (255, 255, 255)         # White panels
MAZE_BORDER = (52, 73, 94)         # Dark border
ACCENT_COLOR = (52, 152, 219)      # Blue accent

# Wall and path colors
WALL_COLOR = (44, 62, 80)          # Dark walls
PATH_BG = (255, 255, 255)          # White path background
VISITED_COLOR = (174, 214, 241)    # Light blue for visited
EXPLORING_COLOR = (133, 193, 233)  # Medium blue for exploring

# Algorithm visualization delay (milliseconds)
VISUALIZATION_DELAY = 15