# 05.08 Draw Line

## Description

Given a monochrome screen stored as an array of integers (32 pixels per word), draw a horizontal line from pixel x1 to x2 on row y. This maps to LCCI 5.8.

Typical interview angle:
- Identify the start and end 32-bit words covering the line.
- Build bitmasks for partial head and tail words.
- Fill whole middle words with 0xFF.

Reference page: https://leetcode.doocs.org/en/lcci/5.8/

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
7ffffffe
```
