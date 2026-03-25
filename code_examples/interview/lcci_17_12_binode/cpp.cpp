#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    TreeNode* prev = nullptr;

    void inorder(TreeNode* root) {
        if (!root) return;
        inorder(root->left);
        root->left = nullptr;
        prev->right = root;
        prev = root;
        inorder(root->right);
    }

public:
    TreeNode* convertBiNode(TreeNode* root) {
        TreeNode dummy(0);
        prev = &dummy;
        inorder(root);
        return dummy.right;
    }
};

int main() {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->right = new TreeNode(6);
    root->left->left->left = new TreeNode(0);

    Solution sol;
    TreeNode* head = sol.convertBiNode(root);
    while (head) {
        cout << head->val << (head->right ? ' ' : '\n');
        head = head->right;
    }
    return 0;
}
