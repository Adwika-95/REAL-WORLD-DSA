#pragma once
#include <SFML/Graphics.hpp>
#include "Maze.h"
#include "Algorithms.h"

class Visualizer {
public:
    Visualizer();
    void run();

private:
    sf::RenderWindow window;
    Maze maze;

    BFS bfs;
    DFS dfs;
    AStar astar;

    void handleEvents();
    void draw();
};
