# 02.03 Delete Middle Node

## Description

Delete a node from the middle of a singly linked list when only that node is given (not the head). This maps to LCCI 2.3.

Typical interview angle:
- Cannot remove tail with this technique.
- Copy next node's value, then bypass next node.
- Clarify edge-case behavior for null/tail nodes.

Reference page: https://leetcode.doocs.org/en/lcci/2.3/

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
1 2 4 5
```
