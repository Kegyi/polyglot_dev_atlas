#!/usr/bin/env python3
from collections import deque


def main() -> None:
    # Stack: list used as LIFO
    stack: list[int] = []
    for v in [1, 2, 3]:
        stack.append(v)
    print("stack top:", stack[-1])  # 3
    stack.pop()
    print("after pop:", stack[-1])  # 2

    # Queue: deque used as FIFO
    queue: deque[int] = deque()
    for v in [1, 2, 3]:
        queue.append(v)
    print("queue front:", queue[0])  # 1
    queue.popleft()
    print("after dequeue:", queue[0])  # 2


if __name__ == "__main__":
    main()
