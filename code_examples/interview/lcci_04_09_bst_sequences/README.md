# 04.09 BST Sequences

## Description

Return all insertion sequences that could create the same BST. This maps to LCCI 4.9.

Typical interview angle:
- Preserve relative order of elements from left subtree sequence.
- Preserve relative order of elements from right subtree sequence.
- Interleave (weave) left and right lists under current root prefix.

Reference page: https://leetcode.doocs.org/en/lcci/4.9/

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
2 1 3
2 3 1
```
