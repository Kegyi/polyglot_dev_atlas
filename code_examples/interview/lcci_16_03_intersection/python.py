from typing import List

EPS = 1e-9


def less_point(a: List[float], b: List[float]) -> bool:
    if abs(a[0] - b[0]) > EPS:
        return a[0] < b[0]
    return a[1] < b[1] - EPS


def cross(a: List[float], b: List[float], c: List[float]) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a: List[float], b: List[float], p: List[float]) -> bool:
    return (
        abs(cross(a, b, p)) < EPS
        and min(a[0], b[0]) - EPS <= p[0] <= max(a[0], b[0]) + EPS
        and min(a[1], b[1]) - EPS <= p[1] <= max(a[1], b[1]) + EPS
    )


def intersection(start1: List[float], end1: List[float], start2: List[float], end2: List[float]) -> List[float]:
    if less_point(end1, start1):
        start1, end1 = end1, start1
    if less_point(end2, start2):
        start2, end2 = end2, start2

    d1 = cross(start1, end1, start2)
    d2 = cross(start1, end1, end2)
    d3 = cross(start2, end2, start1)
    d4 = cross(start2, end2, end1)

    if ((d1 > EPS and d2 > EPS) or (d1 < -EPS and d2 < -EPS) or
            (d3 > EPS and d4 > EPS) or (d3 < -EPS and d4 < -EPS)):
        return []

    a1 = end1[1] - start1[1]
    b1 = start1[0] - end1[0]
    c1 = a1 * start1[0] + b1 * start1[1]

    a2 = end2[1] - start2[1]
    b2 = start2[0] - end2[0]
    c2 = a2 * start2[0] + b2 * start2[1]

    det = a1 * b2 - a2 * b1
    if abs(det) < EPS:
        candidates = []
        if on_segment(start1, end1, start2):
            candidates.append(start2)
        if on_segment(start1, end1, end2):
            candidates.append(end2)
        if on_segment(start2, end2, start1):
            candidates.append(start1)
        if on_segment(start2, end2, end1):
            candidates.append(end1)
        if not candidates:
            return []
        candidates.sort(key=lambda p: (p[0], p[1]))
        return candidates[0]

    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    p = [x, y]
    return p if on_segment(start1, end1, p) and on_segment(start2, end2, p) else []


def main() -> None:
    print(intersection([0, 0], [1, 0], [1, 1], [0, -1]))


if __name__ == "__main__":
    main()
