#include <iostream>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

int heightOrFail(Node* n) {
    if (!n) return 0;
    int lh = heightOrFail(n->l); if (lh == -1) return -1;
    int rh = heightOrFail(n->r); if (rh == -1) return -1;
    if (lh - rh > 1 || rh - lh > 1) return -1;
    return 1 + (lh > rh ? lh : rh);
}

bool isBalanced(Node* root) { return heightOrFail(root) != -1; }

int main() {
    Node* a = new Node(1); a->l = new Node(2); a->r = new Node(3);
    Node* b = new Node(1); b->l = new Node(2); b->l->l = new Node(3); b->l->l->l = new Node(4);
    std::cout << std::boolalpha << isBalanced(a) << '\n';
    std::cout << std::boolalpha << isBalanced(b) << '\n';
}
