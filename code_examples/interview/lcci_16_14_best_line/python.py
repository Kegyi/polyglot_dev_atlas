from typing import List


def collinear(a: List[int], b: List[int], c: List[int]) -> bool:
    x1, y1 = b[0] - a[0], b[1] - a[1]
    x2, y2 = c[0] - a[0], c[1] - a[1]
    return x1 * y2 == x2 * y1


def best_line(points: List[List[int]]) -> List[int]:
    n = len(points)
    best_i, best_j, best_count = 0, 1, 2
    for i in range(n):
        for j in range(i + 1, n):
            count = 2
            for k in range(j + 1, n):
                if collinear(points[i], points[j], points[k]):
                    count += 1
            if count > best_count or (count == best_count and (i < best_i or (i == best_i and j < best_j))):
                best_i, best_j, best_count = i, j, count
    return [best_i, best_j]


def main() -> None:
    print(best_line([[0, 0], [1, 1], [1, 0], [2, 2]]))


if __name__ == "__main__":
    main()
