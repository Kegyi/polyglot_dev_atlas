# 05.02 Binary Number to String

## Description

Convert a decimal fraction between 0 and 1 to its binary string. Return "ERROR" if it cannot be represented in 32 bits. This maps to LCCI 5.2.

Typical interview angle:
- Repeatedly double and take the integer part as the next bit.
- Terminate when the fraction reaches zero.
- Bound the loop to detect non-terminating representations.

Reference page: https://leetcode.doocs.org/en/lcci/5.2/

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
0.101
ERROR
```
