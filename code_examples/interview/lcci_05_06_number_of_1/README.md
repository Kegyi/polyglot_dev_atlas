# 05.06 Number of 1

## Description

Count the number of bits you must flip to convert integer A to integer B. This maps to LCCI 5.6.

Typical interview angle:
- XOR A and B to isolate differing bits.
- Count 1s in the XOR result (popcount).
- Use `x & (x-1)` trick or language built-in for efficiency.

Reference page: https://leetcode.doocs.org/en/lcci/5.6/

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
2
1
```
