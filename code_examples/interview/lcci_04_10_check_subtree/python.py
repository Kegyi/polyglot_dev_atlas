class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def same(a: Node | None, b: Node | None) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)


def is_subtree(t1: Node | None, t2: Node | None) -> bool:
    if t2 is None:
        return True
    if t1 is None:
        return False
    if same(t1, t2):
        return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)


def main() -> None:
    t1 = Node(3)
    t1.left = Node(4); t1.right = Node(5)
    t1.left.left = Node(1); t1.left.right = Node(2)

    t2 = Node(4); t2.left = Node(1); t2.right = Node(2)
    t3 = Node(4); t3.left = Node(1); t3.right = Node(3)

    print(is_subtree(t1, t2))
    print(is_subtree(t1, t3))


if __name__ == "__main__":
    main()
