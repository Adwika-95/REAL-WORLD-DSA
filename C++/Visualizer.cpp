#include "Visualizer.h"
#include "Constants.h"

Visualizer::Visualizer()
    : window(sf::VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), "AlgoMaze C++"),
      maze(MAZE_ROWS, MAZE_COLS) {

    maze.generate();
    maze.start = {0, 0};
    maze.end = {MAZE_ROWS-1, MAZE_COLS-1};
}

void Visualizer::handleEvents() {
    sf::Event e;
    while (window.pollEvent(e)) {
        if (e.type == sf::Event::Closed)
            window.close();
        if (e.type == sf::Event::KeyPressed) {
            if (e.key.code == sf::Keyboard::B) bfs.solve(maze);
            if (e.key.code == sf::Keyboard::D) dfs.solve(maze);
            if (e.key.code == sf::Keyboard::A) astar.solve(maze);
        }
    }
}

void Visualizer::draw() {
    window.clear(BACKGROUND);
    maze.draw(window);
    window.display();
}

void Visualizer::run() {
    while (window.isOpen()) {
        handleEvents();
        draw();
    }
}
