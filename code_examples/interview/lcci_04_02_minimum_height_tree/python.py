class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def build(nums: list[int], lo: int, hi: int) -> Node | None:
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    root = Node(nums[mid])
    root.left = build(nums, lo, mid - 1)
    root.right = build(nums, mid + 1, hi)
    return root


def inorder(root: Node | None) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def main() -> None:
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(" ".join(map(str, inorder(build(nums, 0, len(nums) - 1)))))


if __name__ == "__main__":
    main()
