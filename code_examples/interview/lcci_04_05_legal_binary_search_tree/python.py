class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def is_valid(node: Node | None, lo: int, hi: int) -> bool:
    if node is None:
        return True
    if not (lo < node.val < hi):
        return False
    return is_valid(node.left, lo, node.val) and is_valid(node.right, node.val, hi)


def main() -> None:
    ok = Node(5); ok.left = Node(3); ok.right = Node(7)
    bad = Node(5); bad.left = Node(3); bad.right = Node(7); bad.left.right = Node(6)
    print(is_valid(ok, -10**18, 10**18))
    print(is_valid(bad, -10**18, 10**18))


if __name__ == "__main__":
    main()
