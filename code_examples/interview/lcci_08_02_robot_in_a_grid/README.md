# 08.02 Robot in a Grid

## Description

Imagine a robot sitting on the upper left corner of an `r x c` grid. The robot can only move in two directions, right and down, but certain cells are off limits such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right. The grid has 0 for open cells and 1 for obstacles. Return the path as an array of `[row, col]` coordinates, or an empty array if no path exists.

**Example:**
```
Input: obstacle = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0],[0,1],[0,2],[1,2],[2,2]]
```

**Note:** `r, c <= 100`

## Implementations

- [C++](cpp.cpp)
- [Python](python.py)
- [Go](go.go)
- [TypeScript](typescript.ts)
- [Scala](scala.scala)

## Expected output

```
[[0,0],[0,1],[0,2],[1,2],[2,2]]
```
