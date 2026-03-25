#include <iostream>
#include <queue>
#include <vector>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

std::vector<std::vector<int>> listOfDepth(Node* root) {
    if (!root) return {};
    std::vector<std::vector<int>> out;
    std::queue<Node*> q; q.push(root);
    while (!q.empty()) {
        int n = static_cast<int>(q.size());
        std::vector<int> level;
        while (n--) {
            Node* cur = q.front(); q.pop();
            level.push_back(cur->v);
            if (cur->l) q.push(cur->l);
            if (cur->r) q.push(cur->r);
        }
        out.push_back(level);
    }
    return out;
}

int main() {
    Node* root = new Node(1);
    root->l = new Node(2); root->r = new Node(3);
    root->l->l = new Node(4); root->l->r = new Node(5);
    root->r->l = new Node(6); root->r->r = new Node(7);
    auto levels = listOfDepth(root);
    for (size_t i = 0; i < levels.size(); ++i) {
        if (i) std::cout << " | ";
        for (size_t j = 0; j < levels[i].size(); ++j) {
            if (j) std::cout << ' ';
            std::cout << levels[i][j];
        }
    }
    std::cout << '\n';
}
