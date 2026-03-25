#include <iostream>
#include <queue>

struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : value(v), left(nullptr), right(nullptr) {}
};

TreeNode* insert(TreeNode* root, int value) {
    if (!root) return new TreeNode(value);
    if (value < root->value) root->left  = insert(root->left,  value);
    else                     root->right = insert(root->right, value);
    return root;
}

void inOrder(TreeNode* root) {
    if (!root) return;
    inOrder(root->left);
    std::cout << root->value << ' ';
    inOrder(root->right);
}

void bfs(TreeNode* root) {
    if (!root) return;
    std::queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        std::cout << node->value << ' ';
        if (node->left)  q.push(node->left);
        if (node->right) q.push(node->right);
    }
}

int main() {
    TreeNode* root = nullptr;
    for (int v : {5, 3, 7, 1, 4}) root = insert(root, v);
    std::cout << "in-order: "; inOrder(root); std::cout << "\n";  // 1 3 4 5 7
    std::cout << "bfs:      "; bfs(root);     std::cout << "\n";  // 5 3 7 1 4
    return 0;
}
