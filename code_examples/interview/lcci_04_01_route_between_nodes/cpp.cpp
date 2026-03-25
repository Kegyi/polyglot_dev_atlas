#include <iostream>
#include <queue>
#include <vector>

bool hasRoute(int n, const std::vector<std::pair<int, int>>& edges, int start, int target) {
    std::vector<std::vector<int>> g(n);
    for (auto [u, v] : edges) g[u].push_back(v);
    std::vector<int> seen(n, 0);
    std::queue<int> q;
    q.push(start);
    seen[start] = 1;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (u == target) return true;
        for (int v : g[u]) if (!seen[v]) { seen[v] = 1; q.push(v); }
    }
    return false;
}

int main() {
    std::vector<std::pair<int, int>> edges{{0,1},{0,2},{1,3},{2,4}};
    std::cout << std::boolalpha << hasRoute(5, edges, 0, 4) << '\n';
    std::cout << std::boolalpha << hasRoute(5, edges, 3, 4) << '\n';
}
