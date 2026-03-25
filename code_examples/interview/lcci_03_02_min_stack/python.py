class MinStack:
    def __init__(self) -> None:
        self.values: list[int] = []
        self.mins: list[int] = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        if not self.values:
            return
        if self.values[-1] == self.mins[-1]:
            self.mins.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1] if self.values else -1

    def get_min(self) -> int:
        return self.mins[-1] if self.mins else -1


def main() -> None:
    st = MinStack()
    st.push(3)
    st.push(5)
    st.push(2)
    st.push(2)
    print(st.get_min())
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())


if __name__ == "__main__":
    main()
