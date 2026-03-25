package main

import "fmt"

func hasRoute(n int, edges [][2]int, start int, target int) bool {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
	}
	seen := make([]bool, n)
	q := []int{start}
	seen[start] = true
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		if u == target {
			return true
		}
		for _, v := range g[u] {
			if !seen[v] {
				seen[v] = true
				q = append(q, v)
			}
		}
	}
	return false
}

func main() {
	edges := [][2]int{{0, 1}, {0, 2}, {1, 3}, {2, 4}}
	fmt.Println(hasRoute(5, edges, 0, 4))
	fmt.Println(hasRoute(5, edges, 3, 4))
}
