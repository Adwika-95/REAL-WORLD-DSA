# Sudoku Game

A simple Python Sudoku game and solver with visualization.

## Features
- Play Sudoku interactively
- Visualize solving steps
- Multiple puzzles included
- Modular board and solver logic

## Requirements
- Python 3.8+
- Tkinter (usually included with Python)

## Getting Started
1. Clone this repository or copy the folder.
2. (Optional) Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## File Structure
- `main.py` — Entry point for the game
- `sudoku_board.py` — Board logic and UI
- `sudoku_solver.py` — Solver algorithms
- `sudoku_visualizer.py` — Visualization logic
- `puzzles.py` — Sample Sudoku puzzles
- `constants.py` — App constants

## How to Use
- Launch the app and select a puzzle.
- Play manually or watch the solver in action.
- Visualize each solving step interactively.

## How Sudoku Solver Works: DFS with Backtracking

The Sudoku solver uses a method called Depth-First Search (DFS) with backtracking:

- **DFS** means the solver tries to fill each empty cell by going as deep as possible, one cell at a time.
- **Backtracking** means if the solver reaches a point where no valid number can be placed, it goes back ("undoes" the last step) and tries a different number.

Imagine solving a puzzle by making guesses and, if you get stuck, erasing your last guess and trying something else. This way, the solver explores all possible solutions until it finds one that works!

## License
MIT