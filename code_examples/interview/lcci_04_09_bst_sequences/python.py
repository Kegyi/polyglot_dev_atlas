from collections import deque


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def weave(first: deque[int], second: deque[int], prefix: list[int], out: list[list[int]]) -> None:
    if not first or not second:
        out.append(prefix + list(first) + list(second))
        return

    h1 = first.popleft()
    weave(first, second, prefix + [h1], out)
    first.appendleft(h1)

    h2 = second.popleft()
    weave(first, second, prefix + [h2], out)
    second.appendleft(h2)


def all_seq(root: Node | None) -> list[list[int]]:
    if root is None:
        return [[]]
    left = all_seq(root.left)
    right = all_seq(root.right)
    result: list[list[int]] = []
    for l in left:
        for r in right:
            weaved: list[list[int]] = []
            weave(deque(l), deque(r), [root.val], weaved)
            result.extend(weaved)
    return result


def main() -> None:
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    for seq in all_seq(root):
        print(*seq)


if __name__ == "__main__":
    main()
