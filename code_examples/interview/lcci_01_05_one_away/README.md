# 01.05 One Away

## Description

Decide whether two strings are at most one edit apart, where an edit is insert, delete, or replace one character. This maps to LCCI 1.5 and is a classic two-pointer case analysis problem.

Typical interview angle:
- Handle equal-length and length-diff-by-one cases separately.
- Stop early after a second mismatch.
- Keep O(n) time and O(1) extra space.

Reference page: https://leetcode.doocs.org/en/lcci/1.5/

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
pale vs ple -> true
pales vs pale -> true
pale vs bake -> false
```
