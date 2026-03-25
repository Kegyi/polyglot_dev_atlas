from typing import List


def cut_squares(square1: List[int], square2: List[int]) -> List[float]:
    x1, y1, s1 = square1
    x2, y2, s2 = square2

    cx1, cy1 = x1 + s1 / 2.0, y1 + s1 / 2.0
    cx2, cy2 = x2 + s2 / 2.0, y2 + s2 / 2.0

    eps = 1e-9
    if abs(cx1 - cx2) < eps:
        x = cx1
        y_bottom = min(y1, y2)
        y_top = max(y1 + s1, y2 + s2)
        return [x, y_bottom, x, y_top]

    k = (cy2 - cy1) / (cx2 - cx1)
    b = cy1 - k * cx1

    if abs(k) <= 1:
        px1 = min(x1, x2)
        px2 = max(x1 + s1, x2 + s2)
        py1 = k * px1 + b
        py2 = k * px2 + b
    else:
        py1 = min(y1, y2)
        py2 = max(y1 + s1, y2 + s2)
        px1 = (py1 - b) / k
        px2 = (py2 - b) / k

    if px1 > px2 or (abs(px1 - px2) < eps and py1 > py2):
        px1, px2 = px2, px1
        py1, py2 = py2, py1

    return [px1, py1, px2, py2]


def main() -> None:
    print(cut_squares([-1, -1, 2], [0, -1, 2]))


if __name__ == "__main__":
    main()
