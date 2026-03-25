#include <iostream>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

Node* inorderSuccessor(Node* root, int p) {
    Node* ans = nullptr;
    while (root) {
        if (p < root->v) { ans = root; root = root->l; }
        else root = root->r;
    }
    return ans;
}

int main() {
    Node* root = new Node(5);
    root->l = new Node(3); root->r = new Node(7);
    root->l->l = new Node(2); root->l->r = new Node(4);
    Node* s1 = inorderSuccessor(root, 3);
    Node* s2 = inorderSuccessor(root, 7);
    std::cout << (s1 ? s1->v : -1) << '\n';
    std::cout << (s2 ? s2->v : -1) << '\n';
}
