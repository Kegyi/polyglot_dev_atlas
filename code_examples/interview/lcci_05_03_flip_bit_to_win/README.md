# 05.03 Flip Bit to Win

## Description

Find the length of the longest sequence of 1s you could create by flipping exactly one 0 bit. This maps to LCCI 5.3.

Typical interview angle:
- Track current run of 1s and previous run separated by exactly one 0.
- Slide window: when a 0 is seen, previous = current and current = 0.
- Best answer is prev + 1 (flipped 0) + cur.

Reference page: https://leetcode.doocs.org/en/lcci/5.3/

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
8
4
```
