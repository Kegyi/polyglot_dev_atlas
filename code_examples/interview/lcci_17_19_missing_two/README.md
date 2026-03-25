# 17.19. Missing Two

**Source:** https://leetcode.doocs.org/en/lcci/17.19/

## Problem

You are given an array with all the numbers from 1 to N appearing exactly once, except for two numbers that are missing. Find the two missing numbers.

## Approach

XOR-based solution. XOR all array elements and all numbers 1..N to get `xor = a ^ b`. Find a differing bit (`diff = xor & -xor`). Partition all values by that bit, XOR each partition separately to recover `a` and `b`.

**Time:** O(n) | **Space:** O(1)
