#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional[Node] = field(default=None, repr=False)


def print_list(head: Optional[Node]) -> None:
    parts: list[str] = []
    cur = head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    print(" -> ".join(parts))


def prepend(head: Optional[Node], value: int) -> Node:
    return Node(value=value, next=head)


def remove_value(head: Optional[Node], value: int) -> Optional[Node]:
    if head is None:
        return None
    if head.value == value:
        return head.next
    head.next = remove_value(head.next, value)
    return head


def main() -> None:
    head: Optional[Node] = None
    for v in [3, 2, 1]:
        head = prepend(head, v)  # 1 -> 2 -> 3
    print_list(head)
    head = remove_value(head, 2)
    print_list(head)  # 1 -> 3


if __name__ == "__main__":
    main()
