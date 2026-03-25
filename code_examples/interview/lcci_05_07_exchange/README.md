# 05.07 Exchange

## Description

Swap all odd and even bits of an integer with as few instructions as possible. This maps to LCCI 5.7.

Typical interview angle:
- Mask odd-indexed bits (0xAAAA…) and shift right.
- Mask even-indexed bits (0x5555…) and shift left.
- OR the two halves together.

Reference page: https://leetcode.doocs.org/en/lcci/5.7/

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
1
3
```
