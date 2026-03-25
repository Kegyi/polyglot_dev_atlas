package main

type Trie struct {
	children [26]*Trie
	idx      int
}

func newTrie() *Trie {
	return &Trie{idx: -1}
}

func (t *Trie) insert(word string, i int) {
	node := t
	for _, c := range word {
		j := c - 'a'
		if node.children[j] == nil {
			node.children[j] = newTrie()
		}
		node = node.children[j]
	}
	node.idx = i
}

func multiSearch(big string, smalls []string) [][]int {
	trie := newTrie()
	for i, s := range smalls {
		if s != "" {
			trie.insert(s, i)
		}
	}

	ans := make([][]int, len(smalls))
	for i := range ans {
		ans[i] = []int{}
	}

	for i := range big {
		node := trie
		for j := i; j < len(big); j++ {
			k := big[j] - 'a'
			if node.children[k] == nil {
				break
			}
			node = node.children[k]
			if node.idx != -1 {
				ans[node.idx] = append(ans[node.idx], i)
			}
		}
	}
	return ans
}
