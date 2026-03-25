from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    old = image[sr][sc]
    if old == newColor:
        return image
    r, c = len(image), len(image[0])

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or image[i][j] != old:
            return
        image[i][j] = newColor
        dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1)

    dfs(sr, sc)
    return image

def main():
    result = floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
