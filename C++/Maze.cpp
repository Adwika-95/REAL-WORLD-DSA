#include "Maze.h"
#include "Constants.h"
#include <stack>
#include <random>

Maze::Maze(int r, int c) {
    grid.resize(r, std::vector<MazeCell>(c));
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            grid[i][j].row = i;
            grid[i][j].col = j;
        }
}

void Maze::generate() {
    std::stack<MazeCell*> st;
    MazeCell* current = &grid[0][0];
    current->visited = true;
    st.push(current);

    std::mt19937 rng(std::random_device{}());

    while (!st.empty()) {
        current = st.top();
        std::vector<MazeCell*> neighbors;

        int r = current->row, c = current->col;
        if (r > 0 && !grid[r-1][c].visited) neighbors.push_back(&grid[r-1][c]);
        if (r < MAZE_ROWS-1 && !grid[r+1][c].visited) neighbors.push_back(&grid[r+1][c]);
        if (c > 0 && !grid[r][c-1].visited) neighbors.push_back(&grid[r][c-1]);
        if (c < MAZE_COLS-1 && !grid[r][c+1].visited) neighbors.push_back(&grid[r][c+1]);

        if (!neighbors.empty()) {
            MazeCell* next = neighbors[rng() % neighbors.size()];
            next->visited = true;
            st.push(next);
        } else {
            st.pop();
        }
    }
}
