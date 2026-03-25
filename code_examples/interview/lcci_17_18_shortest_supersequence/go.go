package main

func shortestSeq(big []int, small []int) []int {
	need := make(map[int]int)
	for _, x := range small {
		need[x]++
	}
	window := make(map[int]int)
	cnt := len(small)
	j, k, mi := 0, -1, len(big)+1

	for i, x := range big {
		window[x]++
		if need[x] >= window[x] {
			cnt--
		}
		for cnt == 0 {
			if i-j+1 < mi {
				mi = i - j + 1
				k = j
			}
			if need[big[j]] >= window[big[j]] {
				cnt++
			}
			window[big[j]]--
			j++
		}
	}
	if k == -1 {
		return []int{}
	}
	return []int{k, k + mi - 1}
}
