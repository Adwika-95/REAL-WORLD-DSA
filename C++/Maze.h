#pragma once
#include <vector>
#include <SFML/Graphics.hpp>

struct MazeCell {
    int row, col;
    bool visited = false;
    bool isPath = false;
    bool isVisitedSearch = false;

    bool walls[4] = {true, true, true, true}; 
    // 0=top, 1=right, 2=bottom, 3=left
};

class Maze {
public:
    Maze(int r, int c);
    void generate();
    std::vector<MazeCell*> getNeighbors(MazeCell* cell);
    void draw(sf::RenderWindow& window);

    std::vector<std::vector<MazeCell>> grid;
    std::pair<int,int> start, end;
};
