#include <iostream>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

Node* lca(Node* root, int p, int q) {
    if (!root || root->v == p || root->v == q) return root;
    Node* left = lca(root->l, p, q);
    Node* right = lca(root->r, p, q);
    if (left && right) return root;
    return left ? left : right;
}

int main() {
    Node* root = new Node(3);
    root->l = new Node(5); root->r = new Node(1);
    root->l->l = new Node(6); root->l->r = new Node(2);
    root->r->l = new Node(0); root->r->r = new Node(8);

    std::cout << lca(root, 6, 2)->v << '\n';
    std::cout << lca(root, 6, 8)->v << '\n';
}
