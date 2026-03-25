# 01.09 String Rotation

## Description

Check whether one string is a rotation of another using a single substring test. The standard trick is to test whether `s2` appears in `s1 + s1` after confirming equal lengths. This maps to LCCI 1.9.

Typical interview angle:
- Explain why doubling captures all rotations.
- Handle unequal lengths and empty strings correctly.
- Keep the solution concise and linear in practice.

Reference page: https://leetcode.doocs.org/en/lcci/1.9/

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
waterbottle vs erbottlewat -> true
aa vs aba -> false
```
