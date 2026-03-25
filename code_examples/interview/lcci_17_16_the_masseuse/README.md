# 17.16. The Masseuse

**Source:** https://leetcode.doocs.org/en/lcci/17.16/

## Problem

A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. She needs a 15-minute break between appointments and therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appointment requests (all multiples of 15 minutes, none overlap, and none can be moved), find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.

## Approach

Classic House Robber DP. Keep two states: `f` = best if we skip last, `g` = best if we take last. For each duration `x`: `f, g = g + x, max(f, g)`. Return `max(f, g)`.

**Time:** O(n) | **Space:** O(1)
