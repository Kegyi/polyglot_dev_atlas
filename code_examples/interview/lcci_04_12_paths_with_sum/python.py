class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def path_sum(root: Node | None, target: int) -> int:
    counts: dict[int, int] = {0: 1}

    def dfs(node: Node | None, prefix: int) -> int:
        if node is None:
            return 0
        prefix += node.val
        res = counts.get(prefix - target, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
        res += dfs(node.left, prefix)
        res += dfs(node.right, prefix)
        counts[prefix] -= 1
        return res

    return dfs(root, 0)


def main() -> None:
    root = Node(10)
    root.left = Node(5); root.right = Node(-3)
    root.left.left = Node(3); root.left.right = Node(2)
    root.right.right = Node(11)
    root.left.left.left = Node(3); root.left.left.right = Node(-2)
    root.left.right.right = Node(1)
    print(path_sum(root, 8))


if __name__ == "__main__":
    main()
