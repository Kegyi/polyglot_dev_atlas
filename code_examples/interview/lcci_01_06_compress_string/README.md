# 01.06 Compress String

## Description

Run-length encode a string by replacing repeated characters with character + count, but return the original string when compression does not reduce length. This maps to LCCI 1.6.

Typical interview angle:
- Track contiguous runs with two pointers.
- Build compressed output in one pass.
- Compare compressed size vs original size before returning.

Reference page: https://leetcode.doocs.org/en/lcci/1.6/

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
aabcccccaaa -> a2b1c5a3
abbccd -> abbccd
```
