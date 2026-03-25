#!/usr/bin/env python3
import random


def main() -> None:
    generator = random.Random(42)
    draws = [generator.randint(1, 10) for _ in range(3)]
    print("draws:", draws)


if __name__ == "__main__":
    main()
