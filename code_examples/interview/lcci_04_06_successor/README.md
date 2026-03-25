# 04.06 Successor

## Description

Find the in-order successor of a node in a BST. This maps to LCCI 4.6.

Typical interview angle:
- If searching by value from root, track latest greater ancestor.
- If node has right child, successor is leftmost in right subtree.
- Be explicit when successor does not exist.

Reference page: https://leetcode.doocs.org/en/lcci/4.6/

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
4
-1
```
