class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def height_or_fail(node: Node | None) -> int:
    if node is None:
        return 0
    lh = height_or_fail(node.left)
    if lh == -1:
        return -1
    rh = height_or_fail(node.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    return 1 + max(lh, rh)


def is_balanced(root: Node | None) -> bool:
    return height_or_fail(root) != -1


def main() -> None:
    a = Node(1); a.left = Node(2); a.right = Node(3)
    b = Node(1); b.left = Node(2); b.left.left = Node(3); b.left.left.left = Node(4)
    print(is_balanced(a))
    print(is_balanced(b))


if __name__ == "__main__":
    main()
