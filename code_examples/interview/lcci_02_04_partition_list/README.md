# 02.04 Partition List

## Description

Partition a linked list around value x so that nodes less than x come before nodes greater than or equal to x. This maps to LCCI 2.4.

Typical interview angle:
- Build two temporary lists (less / greater-or-equal).
- Preserve relative order within each partition.
- Reconnect lists and terminate tail safely.

Reference page: https://leetcode.doocs.org/en/lcci/2.4/

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
3 2 1 5 8 5 10
```
