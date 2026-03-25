package main

func findLadders(beginWord string, endWord string, wordList []string) []string {
	wordSet := make(map[string]bool)
	for _, w := range wordList {
		wordSet[w] = true
	}
	if !wordSet[endWord] {
		return []string{}
	}

	type State struct {
		path []string
	}
	queue := []State{{[]string{beginWord}}}
	visited := map[string]bool{beginWord: true}

	for len(queue) > 0 {
		st := queue[0]
		queue = queue[1:]
		cur := st.path[len(st.path)-1]
		bs := []byte(cur)
		for i := 0; i < len(bs); i++ {
			orig := bs[i]
			for c := byte('a'); c <= byte('z'); c++ {
				if c == orig {
					continue
				}
				bs[i] = c
				nxt := string(bs)
				newPath := append(append([]string{}, st.path...), nxt)
				if nxt == endWord {
					return newPath
				}
				if wordSet[nxt] && !visited[nxt] {
					visited[nxt] = true
					queue = append(queue, State{newPath})
				}
				bs[i] = orig
			}
		}
	}
	return []string{}
}
