# 17.13. Re-Space

**Source:** https://leetcode.doocs.org/en/lcci/17.13/

## Problem

Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a lengthy document. A sentence like "I reset the computer. It still didn't boot!" has become "iresetthecomputeritstilldidntboot'". You'll deal with the punctuation and capi-talization later; right now you need to re-insert the spaces. Most of the words are in a dictionary but a few are not. Given a dictionary (a list of strings) and the document (a string), design an algorithm to unconcatenate the document in a way that minimizes the number of unrecognized characters. Return the minimum number of unrecognized characters.

## Approach

Dynamic programming with a dictionary set. `dp[i]` = minimum unrecognized characters for the first `i` characters. For each position, either treat `sentence[i-1]` as unrecognized (`dp[i] = dp[i-1] + 1`) or find a word ending at `i` in the dictionary (`dp[i] = min(dp[i], dp[j])` where `sentence[j:i]` is in dictionary).

**Time:** O(n²) | **Space:** O(n)
