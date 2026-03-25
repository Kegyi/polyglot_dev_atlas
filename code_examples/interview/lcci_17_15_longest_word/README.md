# 17.15. Longest Word

**Source:** https://leetcode.doocs.org/en/lcci/17.15/

## Problem

Given a list of words, write a program to find the longest word made of other words in the list. If there are more than one answer, return the one that has the smaller lexicographical order. If no answer, return an empty string.

## Approach

Build a set of all words. Sort words by length descending (tie-break lexicographically). For each word, check if it can be built from other words using recursive/DP check with the set (excluding the word itself).

**Time:** O(n * L²) | **Space:** O(n * L)
