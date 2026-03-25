class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def lca(root: Node | None, p: int, q: int) -> Node | None:
    if root is None or root.val == p or root.val == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right


def main() -> None:
    root = Node(3)
    root.left = Node(5); root.right = Node(1)
    root.left.left = Node(6); root.left.right = Node(2)
    root.right.left = Node(0); root.right.right = Node(8)

    print(lca(root, 6, 2).val)
    print(lca(root, 6, 8).val)


if __name__ == "__main__":
    main()
