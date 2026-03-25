package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

var parent map[string]string

func find(x string) string {
	if _, ok := parent[x]; !ok {
		parent[x] = x
	}
	if parent[x] != x {
		parent[x] = find(parent[x])
	}
	return parent[x]
}

func unite(a, b string) {
	pa, pb := find(a), find(b)
	if pa != pb {
		if pa < pb {
			parent[pb] = pa
		} else {
			parent[pa] = pb
		}
	}
}

func trulyMostPopular(names []string, synonyms []string) []string {
	parent = make(map[string]string)
	freq := make(map[string]int)
	for _, s := range names {
		paren := strings.Index(s, "(")
		name := s[:paren]
		count, _ := strconv.Atoi(s[paren+1 : len(s)-1])
		freq[name] = count
	}
	for _, syn := range synonyms {
		s := syn[1 : len(syn)-1]
		comma := strings.Index(s, ",")
		unite(s[:comma], s[comma+1:])
	}
	result := make(map[string]int)
	for name, cnt := range freq {
		result[find(name)] += cnt
	}
	ans := make([]string, 0, len(result))
	for name, cnt := range result {
		ans = append(ans, name+"("+strconv.Itoa(cnt)+")")
	}
	sort.Strings(ans)
	return ans
}

func main() {
	names := []string{"John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"}
	synonyms := []string{"(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"}
	fmt.Println(strings.Join(trulyMostPopular(names, synonyms), " ")) // Chris(36) John(27)
}
