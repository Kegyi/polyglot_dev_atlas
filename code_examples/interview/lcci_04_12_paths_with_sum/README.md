# 04.12 Paths with Sum

## Description

Count downward paths in a binary tree whose sum equals a target. This maps to LCCI 4.12.

Typical interview angle:
- Naive restart DFS at each node is $O(n^2)$ in skewed trees.
- Prefix-sum + hash map gives $O(n)$ average time.
- Carefully backtrack prefix frequencies during recursion unwind.

Reference page: https://leetcode.doocs.org/en/lcci/4.12/

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
3
```
