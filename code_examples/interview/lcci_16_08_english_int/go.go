package main

import "fmt"

var ones = []string{"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
var teens = []string{"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"}
var tens = []string{"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"}
var units = []string{"", "Thousand", "Million", "Billion"}

func below1000(n int) string {
	parts := make([]string, 0)
	if n >= 100 {
		parts = append(parts, ones[n/100], "Hundred")
		n %= 100
	}
	if n >= 20 {
		parts = append(parts, tens[n/10])
		if n%10 != 0 {
			parts = append(parts, ones[n%10])
		}
	} else if n >= 10 {
		parts = append(parts, teens[n-10])
	} else if n > 0 {
		parts = append(parts, ones[n])
	}
	ans := ""
	for i, p := range parts {
		if i > 0 {
			ans += " "
		}
		ans += p
	}
	return ans
}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	if num < 0 {
		return "Negative " + numberToWords(-num)
	}

	parts := make([]string, 0)
	unit := 0
	for num > 0 {
		chunk := num % 1000
		if chunk > 0 {
			piece := below1000(chunk)
			if units[unit] != "" {
				piece += " " + units[unit]
			}
			parts = append(parts, piece)
		}
		num /= 1000
		unit++
	}

	ans := ""
	for i := len(parts) - 1; i >= 0; i-- {
		if ans != "" {
			ans += " "
		}
		ans += parts[i]
	}
	return ans
}

func main() {
	fmt.Println(numberToWords(123))
	fmt.Println(numberToWords(12345))
	fmt.Println(numberToWords(-1000010))
}
