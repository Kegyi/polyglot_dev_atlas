# 17.14. Smallest K

**Source:** https://leetcode.doocs.org/en/lcci/17.14/

## Problem

Design an algorithm to find the smallest K numbers in an array. Return these numbers in any order.

## Approach

Sort the array and return the first `k` elements. For larger inputs, a max-heap of size `k` is more efficient: push each element, pop the max when size exceeds `k`.

**Time:** O(n log n) sort / O(n log k) heap | **Space:** O(k)
