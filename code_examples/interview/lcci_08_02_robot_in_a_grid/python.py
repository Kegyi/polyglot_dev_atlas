from typing import List

def pathWithObstacles(obstacleGrid: List[List[int]]) -> List[List[int]]:
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    path = []
    visited = [[False] * c for _ in range(r)]

    def dfs(i, j):
        if i >= r or j >= c or obstacleGrid[i][j] == 1 or visited[i][j]:
            return False
        visited[i][j] = True
        path.append([i, j])
        if i == r - 1 and j == c - 1:
            return True
        if dfs(i + 1, j) or dfs(i, j + 1):
            return True
        path.pop()
        return False

    dfs(0, 0)
    return path

def main():
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(pathWithObstacles(grid))

if __name__ == "__main__":
    main()
