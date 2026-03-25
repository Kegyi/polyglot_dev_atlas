from collections import deque


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def list_of_depth(root: Node | None) -> list[list[int]]:
    if root is None:
        return []
    out: list[list[int]] = []
    q: deque[Node] = deque([root])
    while q:
        level: list[int] = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        out.append(level)
    return out


def main() -> None:
    root = Node(1)
    root.left, root.right = Node(2), Node(3)
    root.left.left, root.left.right = Node(4), Node(5)
    root.right.left, root.right.right = Node(6), Node(7)
    print(" | ".join(" ".join(map(str, lvl)) for lvl in list_of_depth(root)))


if __name__ == "__main__":
    main()
