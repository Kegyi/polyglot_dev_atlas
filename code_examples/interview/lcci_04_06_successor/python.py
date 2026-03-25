class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def inorder_successor(root: Node | None, p: int) -> Node | None:
    ans = None
    while root is not None:
        if p < root.val:
            ans = root
            root = root.left
        else:
            root = root.right
    return ans


def main() -> None:
    root = Node(5)
    root.left = Node(3); root.right = Node(7)
    root.left.left = Node(2); root.left.right = Node(4)
    s1 = inorder_successor(root, 3)
    s2 = inorder_successor(root, 7)
    print(s1.val if s1 else -1)
    print(s2.val if s2 else -1)


if __name__ == "__main__":
    main()
