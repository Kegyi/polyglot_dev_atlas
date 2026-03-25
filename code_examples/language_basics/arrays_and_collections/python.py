#!/usr/bin/env python3

def main() -> None:
    values = [1, 2, 3, 4, 5]
    print("original:", values)

    doubled = [x * 2 for x in values]
    evens = [x for x in doubled if x % 2 == 0]

    print("doubled:", doubled)
    print("evens:", evens)
    print("sum of evens in doubled:", sum(evens))


if __name__ == "__main__":
    main()
