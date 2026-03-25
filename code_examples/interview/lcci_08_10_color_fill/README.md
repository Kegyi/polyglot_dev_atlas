# 08.10 Color Fill

## Description

Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color.

**Example:**
```
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]
```

**Note:** The length of `image` and `image[0]` will be in the range `[1, 50]`.

## Implementations

- [C++](cpp.cpp)
- [Python](python.py)
- [Go](go.go)
- [TypeScript](typescript.ts)
- [Scala](scala.scala)

## Expected output

```
[2,2,2]
[2,2,0]
[2,0,1]
```
