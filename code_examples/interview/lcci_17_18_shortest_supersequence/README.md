# 17.18. Shortest Supersequence

**Source:** https://leetcode.doocs.org/en/lcci/17.18/

## Problem

You have two arrays, one shorter (with all distinct elements) and one longer. Find the shortest subarray in the longer array that contains all the elements in the shorter array. The items can appear in any order. Return the indexes of the leftmost and the shortest subarray, or an empty array if no subarray exists.

## Approach

Sliding window (minimum window). Use a counter of `small` elements needed. Expand right pointer, decrement count when a needed element is matched. When all matched, shrink left pointer while still valid. Track minimum window index.

**Time:** O(n) | **Space:** O(m)
