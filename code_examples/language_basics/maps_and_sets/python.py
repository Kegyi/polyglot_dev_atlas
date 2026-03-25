#!/usr/bin/env python3

def main() -> None:
    counts = {"apple": 2, "banana": 1}
    counts["apple"] += 3

    tags = {"fruit", "food"}
    tags.add("fresh")

    print("apple count:", counts["apple"])
    print("all map entries:", sorted(counts.items()))
    print("all set entries:", sorted(tags))


if __name__ == "__main__":
    main()
