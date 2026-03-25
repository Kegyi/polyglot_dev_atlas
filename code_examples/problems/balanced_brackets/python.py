def is_balanced(s: str) -> bool:
    close_to_open = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in close_to_open:
            if not stack or stack[-1] != close_to_open[ch]:
                return False
            stack.pop()

    return not stack


def main() -> None:
    input_1 = "([{}])(()[]){}"
    input_2 = "([)]"

    print(f"input_1 valid: {str(is_balanced(input_1)).lower()}")
    print(f"input_2 valid: {str(is_balanced(input_2)).lower()}")


if __name__ == "__main__":
    main()
