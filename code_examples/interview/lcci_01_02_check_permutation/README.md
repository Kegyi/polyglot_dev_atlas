# 01.02 Check Permutation

## Description

Check whether two strings are permutations of each other, meaning they contain the same characters with the same frequencies. This maps to LCCI 1.2 and emphasizes counting-based comparisons.

Typical interview angle:
- Early reject using length.
- Compare frequency histograms in O(n).
- Discuss trade-offs between hash maps and fixed-size arrays.

Reference page: https://leetcode.doocs.org/en/lcci/1.2/

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
abcde vs edcba -> true
abc vs abz -> false
```
