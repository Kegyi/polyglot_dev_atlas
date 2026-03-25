# 01.08 Zero Matrix

## Description

Given an m x n matrix, if an element is zero, set its entire row and column to zero. This maps to LCCI 1.8 and tests careful two-phase mutation.

Typical interview angle:
- Avoid corrupting future decisions while scanning.
- Use marker rows/columns or explicit row/column sets.
- Discuss O(m+n) extra memory vs O(1) marker optimization.

Reference page: https://leetcode.doocs.org/en/lcci/1.8/

## Implementations

- cpp.cpp
- go.go
- python.py
- typescript.ts
- scala.scala

## Input

No input file is required.

## Expected output

```text
1 0 3
0 0 0
7 0 9
```
