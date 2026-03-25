class StackOfPlates:
    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.stacks: list[list[int]] = []

    def push(self, val: int) -> None:
        if self.cap <= 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self) -> int:
        return self.pop_at(len(self.stacks) - 1)

    def pop_at(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return val


def main() -> None:
    s = StackOfPlates(2)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop_at(0))
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == "__main__":
    main()
