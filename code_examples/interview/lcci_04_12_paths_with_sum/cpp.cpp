#include <iostream>
#include <unordered_map>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

int dfs(Node* node, int target, long long prefix, std::unordered_map<long long, int>& cnt) {
    if (!node) return 0;
    prefix += node->v;
    int res = 0;
    auto it = cnt.find(prefix - target);
    if (it != cnt.end()) res += it->second;

    cnt[prefix]++;
    res += dfs(node->l, target, prefix, cnt);
    res += dfs(node->r, target, prefix, cnt);
    cnt[prefix]--;

    return res;
}

int pathSum(Node* root, int target) {
    std::unordered_map<long long, int> cnt;
    cnt[0] = 1;
    return dfs(root, target, 0, cnt);
}

int main() {
    Node* root = new Node(10);
    root->l = new Node(5); root->r = new Node(-3);
    root->l->l = new Node(3); root->l->r = new Node(2);
    root->r->r = new Node(11);
    root->l->l->l = new Node(3); root->l->l->r = new Node(-2);
    root->l->r->r = new Node(1);

    std::cout << pathSum(root, 8) << '\n';
}
