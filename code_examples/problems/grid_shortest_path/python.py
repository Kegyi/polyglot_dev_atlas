from collections import deque


def shortest_path_steps(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    dist = [[-1] * cols for _ in range(rows)]
    q: deque[tuple[int, int]] = deque([(0, 0)])
    dist[0][0] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        r, c = q.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if grid[nr][nc] == 1 or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    return -1


def main() -> None:
    grid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]

    print(f"shortest steps: {shortest_path_steps(grid)}")


if __name__ == "__main__":
    main()
