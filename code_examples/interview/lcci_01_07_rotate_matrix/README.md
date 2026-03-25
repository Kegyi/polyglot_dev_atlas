# 01.07 Rotate Matrix

## Description

Rotate an N x N matrix 90 degrees clockwise in place. This maps to LCCI 1.7 and targets index reasoning for layered matrix swaps.

Typical interview angle:
- Work layer by layer from outer ring to inner ring.
- Perform 4-way swaps per step.
- Keep O(1) extra memory for in-place rotation.

Reference page: https://leetcode.doocs.org/en/lcci/1.7/

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
7 4 1
8 5 2
9 6 3
```
