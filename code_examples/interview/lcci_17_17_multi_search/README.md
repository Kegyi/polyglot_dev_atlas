# 17.17. Multi Search

**Source:** https://leetcode.doocs.org/en/lcci/17.17/

## Problem

Given a string `big` and an array of small strings `smalls`, design a method to find the location of each small string in `big`. Return an array of lists of locations, where `locations[i]` is all locations of `smalls[i]`.

## Approach

Build a Trie from all `smalls`. For each starting position `i` in `big`, walk the trie from that position, recording any word-end matches. Map word index via stored values in trie nodes.

**Time:** O(|big| * max_small + sum_smalls) | **Space:** O(sum_smalls)
