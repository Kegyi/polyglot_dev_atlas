class BinaryIndexedTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, index: int, delta: int) -> None:
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class StreamRank:
    def __init__(self) -> None:
        self.bit = BinaryIndexedTree(50010)

    def track(self, x: int) -> None:
        self.bit.update(x + 1, 1)

    def get_rank_of_number(self, x: int) -> int:
        return self.bit.query(x + 1)


def main() -> None:
    stream_rank = StreamRank()
    print(stream_rank.get_rank_of_number(1))
    stream_rank.track(0)
    print(stream_rank.get_rank_of_number(0))


if __name__ == "__main__":
    main()
