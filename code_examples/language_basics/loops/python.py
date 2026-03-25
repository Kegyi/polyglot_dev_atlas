#!/usr/bin/env python3

def main() -> None:
    values = [1, 2, 3, 4, 5]

    for i in range(len(values)):
        print("for index:", i, "->", values[i])

    for v in values:
        if v == 3:
            continue
        print("for each:", v)

    i = 0
    while i < len(values):
        if values[i] == 4:
            break
        print("while:", values[i])
        i += 1

    c = 0
    while True:
        print("do-while style iteration:", c)
        c += 1
        if c >= 2:
            break


if __name__ == "__main__":
    main()
