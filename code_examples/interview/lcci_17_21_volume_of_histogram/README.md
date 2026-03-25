# 17.21. Volume of Histogram

**Source:** https://leetcode.doocs.org/en/lcci/17.21/

## Problem

Imagine a histogram (bar graph). Design an algorithm to compute the volume of water it could hold if someone poured water across the top. You can assume that each histogram bar has width 1.

(This is the classic "Trapping Rain Water" problem.)

## Approach

Two-pointer approach: maintain `left` and `right` pointers, and `leftMax`/`rightMax`. Move the pointer with smaller max inward, accumulating `max - height` as trapped water.

**Time:** O(n) | **Space:** O(1)
