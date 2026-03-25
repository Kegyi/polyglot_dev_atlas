# 10.10 Rank from Stream

## Description

Read integers from a stream and support two operations:
- `track(x)`: record a new number
- `getRankOfNumber(x)`: return how many tracked numbers are less than or equal to `x`

**Example:**
```
Input:
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
Output: [null, 0, null, 1]
```

**Notes:**
- `x <= 50000`
- At most `2000` calls are made in total.

## Implementations

- [C++](cpp.cpp)
- [Python](python.py)
- [Go](go.go)
- [TypeScript](typescript.ts)
- [Scala](scala.scala)

## Expected output

```
0
1
```
