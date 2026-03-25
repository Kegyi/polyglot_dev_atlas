package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "strings"
)

func main() {
    path := "data.txt"
    if len(os.Args) > 1 { path = os.Args[1] }
    f, err := os.Open(path)
    if err != nil { fmt.Println("Error:", err); os.Exit(1) }
    defer f.Close()
    scanner := bufio.NewScanner(f)
    scanner.Split(bufio.ScanWords)
    counts := map[string]int{}
    for scanner.Scan() {
        w := strings.ToLower(scanner.Text())
        // keep only letters
        filtered := ""
        for _, r := range w { if (r >= 'a' && r <= 'z') || (r >= '0' && r <= '9') { filtered += string(r) } }
        if filtered != "" { counts[filtered]++ }
    }
    type P struct{ K string; V int }
    arr := make([]P, 0, len(counts))
    for k, v := range counts { arr = append(arr, P{k, v}) }
    sort.Slice(arr, func(i, j int) bool { return arr[i].V > arr[j].V })
    for _, p := range arr { fmt.Printf("%s: %d\n", p.K, p.V) }
}
