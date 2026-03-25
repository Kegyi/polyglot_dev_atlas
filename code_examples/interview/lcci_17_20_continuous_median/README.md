# 17.20. Continuous Median

**Source:** https://leetcode.doocs.org/en/lcci/17.20/

## Problem

Numbers are randomly generated and passed to a method. Write a program to find and maintain the median value as new values are generated.

Implement `MedianFinder`: `addNum(num)` and `findMedian()`.

## Approach

Maintain two heaps: a max-heap (lower half) and a min-heap (upper half). Always keep them balanced (sizes differ by at most 1). `findMedian` returns top of the larger heap or average of both tops.

**Time:** O(log n) addNum, O(1) findMedian | **Space:** O(n)
