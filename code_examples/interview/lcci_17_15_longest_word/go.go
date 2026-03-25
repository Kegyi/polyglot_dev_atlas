package main

import "sort"

func longestWord(words []string) string {
	wordSet := make(map[string]bool)
	for _, w := range words {
		wordSet[w] = true
	}

	var canBuild func(w string) bool
	canBuild = func(w string) bool {
		if w == "" {
			return true
		}
		for i := 1; i <= len(w); i++ {
			if wordSet[w[:i]] && canBuild(w[i:]) {
				return true
			}
		}
		return false
	}

	sort.Slice(words, func(i, j int) bool {
		if len(words[i]) != len(words[j]) {
			return len(words[i]) > len(words[j])
		}
		return words[i] < words[j]
	})

	for _, w := range words {
		delete(wordSet, w)
		if canBuild(w) {
			return w
		}
		wordSet[w] = true
	}
	return ""
}
