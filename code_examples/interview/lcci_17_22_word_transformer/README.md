# 17.22. Word Transformer

**Source:** https://leetcode.doocs.org/en/lcci/17.22/

## Problem

Given two words of equal length that are in a dictionary, write a method to transform one word into another word by changing only one letter at a time. The new word you get in each step must be in the dictionary. Return each step in the transformation. Return null (or empty) if there is no such transformation.

## Approach

BFS from `start` word. For each word in the queue, try changing each character position to every letter a-z. If the resulting word is in the dictionary set and not yet visited, add it to the queue with the path. If `target` is reached, return the path.

**Time:** O(n * L * 26) | **Space:** O(n * L)
