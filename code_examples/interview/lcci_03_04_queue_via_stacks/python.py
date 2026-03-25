class MyQueue:
    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _move_if_needed(self) -> None:
        if self.out_stack:
            return
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._move_if_needed()
        return self.out_stack.pop() if self.out_stack else -1

    def peek(self) -> int:
        self._move_if_needed()
        return self.out_stack[-1] if self.out_stack else -1

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


def main() -> None:
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.peek())
    print(q.pop())
    print(q.pop())
    print(q.empty())


if __name__ == "__main__":
    main()
