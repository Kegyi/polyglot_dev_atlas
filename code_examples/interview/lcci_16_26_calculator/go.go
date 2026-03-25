package main

import "fmt"

func calculate(s string) int {
	st := make([]int, 0)
	num := 0
	op := byte('+')
	for i := 0; i <= len(s); i++ {
		ch := byte('+')
		if i < len(s) {
			ch = s[i]
		}
		if ch == ' ' {
			continue
		}
		if ch >= '0' && ch <= '9' {
			num = num*10 + int(ch-'0')
			continue
		}
		switch op {
		case '+':
			st = append(st, num)
		case '-':
			st = append(st, -num)
		case '*':
			st[len(st)-1] = st[len(st)-1] * num
		case '/':
			st[len(st)-1] = st[len(st)-1] / num
		}
		op = ch
		num = 0
	}
	ans := 0
	for _, v := range st {
		ans += v
	}
	return ans
}

func main() {
	fmt.Println(calculate("3+2*2"))
	fmt.Println(calculate(" 3/2 "))
	fmt.Println(calculate(" 3+5 / 2 "))
}
