# 01.03 String to URL

## Description

Replace spaces in the meaningful part of a string with `%20`. In the original interview setting, the string buffer often has extra trailing space to support in-place replacement. This maps to LCCI 1.3.

Typical interview angle:
- Respect `trueLength` and ignore trailing buffer space.
- Handle multiple spaces correctly.
- Compare in-place vs out-of-place implementations.

Reference page: https://leetcode.doocs.org/en/lcci/1.3/

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
Mr%20John%20Smith
```
