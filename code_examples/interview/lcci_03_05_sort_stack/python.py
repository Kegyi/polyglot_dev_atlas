def sort_stack(st: list[int]) -> None:
    tmp: list[int] = []
    while st:
        cur = st.pop()
        while tmp and tmp[-1] > cur:
            st.append(tmp.pop())
        tmp.append(cur)
    while tmp:
        st.append(tmp.pop())


def main() -> None:
    st = [3, 1, 4, 2]
    sort_stack(st)
    print(" ".join(str(x) for x in reversed(st)))


if __name__ == "__main__":
    main()
