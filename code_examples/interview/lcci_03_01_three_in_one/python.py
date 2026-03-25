class TripleInOne:
    def __init__(self, stack_size: int) -> None:
        self.size = stack_size
        self.data = [0] * (3 * stack_size)
        self.tops = [0, 0, 0]

    def push(self, stack_num: int, value: int) -> None:
        if self.tops[stack_num] == self.size:
            return
        index = stack_num * self.size + self.tops[stack_num]
        self.data[index] = value
        self.tops[stack_num] += 1

    def pop(self, stack_num: int) -> int:
        if self.tops[stack_num] == 0:
            return -1
        self.tops[stack_num] -= 1
        index = stack_num * self.size + self.tops[stack_num]
        return self.data[index]

    def peek(self, stack_num: int) -> int:
        if self.tops[stack_num] == 0:
            return -1
        index = stack_num * self.size + self.tops[stack_num] - 1
        return self.data[index]

    def is_empty(self, stack_num: int) -> bool:
        return self.tops[stack_num] == 0


def main() -> None:
    stacks = TripleInOne(2)
    stacks.push(0, 10)
    stacks.push(0, 11)
    stacks.push(0, 12)
    stacks.push(1, 20)
    print(stacks.peek(0))
    print(stacks.pop(0))
    print(stacks.pop(0))
    print(stacks.pop(0))
    print(stacks.is_empty(1))


if __name__ == "__main__":
    main()
