# 05.04 Closed Number

## Description

Find the next smaller and next larger integers with the same number of 1 bits. This maps to LCCI 5.4.

Typical interview angle:
- For next larger: find rightmost "01" pattern and swap to "10".
- For next smaller: find rightmost "10" pattern and swap to "01".
- Edge cases: all-1 bit sequences and numbers like powers of 2.

Reference page: https://leetcode.doocs.org/en/lcci/5.4/

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
1
```
