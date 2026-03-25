def calculate(s: str) -> int:
    st = []
    num = 0
    op = "+"
    for ch in s + "+":
        if ch == " ":
            continue
        if ch.isdigit():
            num = num * 10 + int(ch)
            continue
        if op == "+":
            st.append(num)
        elif op == "-":
            st.append(-num)
        elif op == "*":
            st.append(st.pop() * num)
        else:
            st.append(int(st.pop() / num))
        op = ch
        num = 0
    return sum(st)


def main() -> None:
    print(calculate("3+2*2"))
    print(calculate(" 3/2 "))
    print(calculate(" 3+5 / 2 "))


if __name__ == "__main__":
    main()
