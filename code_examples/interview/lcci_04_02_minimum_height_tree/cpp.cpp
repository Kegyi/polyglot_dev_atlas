#include <iostream>
#include <vector>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

Node* build(const std::vector<int>& a, int lo, int hi) {
    if (lo > hi) return nullptr;
    int mid = (lo + hi) / 2;
    Node* root = new Node(a[mid]);
    root->l = build(a, lo, mid - 1);
    root->r = build(a, mid + 1, hi);
    return root;
}

void inorder(Node* n) { if (!n) return; inorder(n->l); std::cout << n->v << ' '; inorder(n->r); }

int main() {
    std::vector<int> nums{1,2,3,4,5,6,7};
    Node* root = build(nums, 0, static_cast<int>(nums.size()) - 1);
    inorder(root);
    std::cout << '\n';
}
