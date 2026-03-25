from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def __init__(self) -> None:
        self.prev: Optional[TreeNode] = None

    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        self.prev = dummy

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.prev.right = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        return dummy.right


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(0)

    head = Solution().convertBiNode(root)
    out = []
    while head:
        out.append(str(head.val))
        head = head.right
    print(' '.join(out))  # 0 1 2 3 4 5 6


if __name__ == "__main__":
    main()
