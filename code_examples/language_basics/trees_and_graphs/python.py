#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TreeNode:
    value: int
    left: Optional[TreeNode] = field(default=None, repr=False)
    right: Optional[TreeNode] = field(default=None, repr=False)


def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def in_order(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    return in_order(root.left) + [root.value] + in_order(root.right)


def bfs(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    result: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    return result


def main() -> None:
    root: Optional[TreeNode] = None
    for v in [5, 3, 7, 1, 4]:
        root = insert(root, v)
    print("in-order:", in_order(root))  # [1, 3, 4, 5, 7]
    print("bfs:     ", bfs(root))       # [5, 3, 7, 1, 4]


if __name__ == "__main__":
    main()
