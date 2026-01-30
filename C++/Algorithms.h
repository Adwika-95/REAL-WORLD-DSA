#pragma once
#include "Maze.h"
#include <SFML/Graphics.hpp>

class Pathfinding {
public:
    virtual bool solve(Maze& maze, sf::RenderWindow& window) = 0;
};

class BFS : public Pathfinding {
public:
    bool solve(Maze& maze, sf::RenderWindow& window) override;
};

class DFS : public Pathfinding {
public:
    bool solve(Maze& maze, sf::RenderWindow& window) override;
};

class AStar : public Pathfinding {
public:
    bool solve(Maze& maze, sf::RenderWindow& window) override;
};
