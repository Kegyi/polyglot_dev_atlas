#include <iostream>
#include <limits>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

bool isValid(Node* n, long long lo, long long hi) {
    if (!n) return true;
    if (n->v <= lo || n->v >= hi) return false;
    return isValid(n->l, lo, n->v) && isValid(n->r, n->v, hi);
}

int main() {
    Node* ok = new Node(5); ok->l = new Node(3); ok->r = new Node(7);
    Node* bad = new Node(5); bad->l = new Node(3); bad->r = new Node(7); bad->l->r = new Node(6);
    std::cout << std::boolalpha << isValid(ok, std::numeric_limits<long long>::min(), std::numeric_limits<long long>::max()) << '\n';
    std::cout << std::boolalpha << isValid(bad, std::numeric_limits<long long>::min(), std::numeric_limits<long long>::max()) << '\n';
}
