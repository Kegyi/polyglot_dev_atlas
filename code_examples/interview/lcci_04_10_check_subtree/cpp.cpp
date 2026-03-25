#include <iostream>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

bool same(Node* a, Node* b) {
    if (!a && !b) return true;
    if (!a || !b) return false;
    return a->v == b->v && same(a->l, b->l) && same(a->r, b->r);
}

bool isSubtree(Node* t1, Node* t2) {
    if (!t2) return true;
    if (!t1) return false;
    if (same(t1, t2)) return true;
    return isSubtree(t1->l, t2) || isSubtree(t1->r, t2);
}

int main() {
    Node* t1 = new Node(3);
    t1->l = new Node(4); t1->r = new Node(5);
    t1->l->l = new Node(1); t1->l->r = new Node(2);

    Node* t2 = new Node(4); t2->l = new Node(1); t2->r = new Node(2);
    Node* t3 = new Node(4); t3->l = new Node(1); t3->r = new Node(3);

    std::cout << std::boolalpha << isSubtree(t1, t2) << '\n';
    std::cout << std::boolalpha << isSubtree(t1, t3) << '\n';
}
