#include "Algorithms.h"
#include <queue>
#include <stack>
#include <unordered_map>
#include <cmath>

bool BFS::solve(Maze& maze) {
    std::queue<MazeCell*> q;
    std::unordered_map<MazeCell*, MazeCell*> parent;

    auto* start = &maze.grid[maze.start.first][maze.start.second];
    auto* end   = &maze.grid[maze.end.first][maze.end.second];

    q.push(start);
    parent[start] = nullptr;

    while (!q.empty()) {
        auto* cur = q.front(); q.pop();
        cur->isVisitedSearch = true;

        if (cur == end) {
            while (cur) { cur->isPath = true; cur = parent[cur]; }
            return true;
        }

        for (auto* n : maze.getNeighbors(cur)) {
            if (!parent.count(n)) {
                parent[n] = cur;
                q.push(n);
            }
        }
    }
    return false;
}

bool DFS::solve(Maze& maze) {
    std::stack<MazeCell*> st;
    std::unordered_map<MazeCell*, MazeCell*> parent;

    auto* start = &maze.grid[maze.start.first][maze.start.second];
    auto* end   = &maze.grid[maze.end.first][maze.end.second];

    st.push(start);
    parent[start] = nullptr;

    while (!st.empty()) {
        auto* cur = st.top(); st.pop();
        cur->isVisitedSearch = true;

        if (cur == end) {
            while (cur) { cur->isPath = true; cur = parent[cur]; }
            return true;
        }

        for (auto* n : maze.getNeighbors(cur)) {
            if (!parent.count(n)) {
                parent[n] = cur;
                st.push(n);
            }
        }
    }
    return false;
}

bool AStar::solve(Maze& maze) {
    auto h = [&](MazeCell* c) {
        return abs(c->row - maze.end.first) + abs(c->col - maze.end.second);
    };

    using Node = std::pair<int, MazeCell*>;
    std::priority_queue<Node, std::vector<Node>, std::greater<>> pq;
    std::unordered_map<MazeCell*, MazeCell*> parent;
    std::unordered_map<MazeCell*, int> g;

    auto* start = &maze.grid[maze.start.first][maze.start.second];
    auto* end   = &maze.grid[maze.end.first][maze.end.second];

    pq.push({0, start});
    g[start] = 0;
    parent[start] = nullptr;

    while (!pq.empty()) {
        auto cur = pq.top().second; pq.pop();
        cur->isVisitedSearch = true;

        if (cur == end) {
            while (cur) { cur->isPath = true; cur = parent[cur]; }
            return true;
        }

        for (auto* n : maze.getNeighbors(cur)) {
            int tg = g[cur] + 1;
            if (!g.count(n) || tg < g[n]) {
                g[n] = tg;
                parent[n] = cur;
                pq.push({tg + h(n), n});
            }
        }
    }
    return false;
}
