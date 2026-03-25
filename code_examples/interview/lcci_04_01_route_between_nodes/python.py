from collections import deque


def has_route(n: int, edges: list[tuple[int, int]], start: int, target: int) -> bool:
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    seen = [False] * n
    q: deque[int] = deque([start])
    seen[start] = True
    while q:
        u = q.popleft()
        if u == target:
            return True
        for v in g[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return False


def main() -> None:
    edges = [(0, 1), (0, 2), (1, 3), (2, 4)]
    print(has_route(5, edges, 0, 4))
    print(has_route(5, edges, 3, 4))


if __name__ == "__main__":
    main()
