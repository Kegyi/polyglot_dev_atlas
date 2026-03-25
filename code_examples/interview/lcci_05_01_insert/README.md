# 05.01 Insert

## Description

Insert bits of integer M into N, replacing bits i through j. This maps to LCCI 5.1.

Typical interview angle:
- Clear target bits in N with a masked complement.
- Shift M into position and OR with cleared N.
- Handle edge cases when j - i + 1 equals the word width.

Reference page: https://leetcode.doocs.org/en/lcci/5.1/

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
1100
19
```
