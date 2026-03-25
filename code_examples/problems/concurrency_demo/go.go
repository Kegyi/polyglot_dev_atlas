package main

import (
    "fmt"
    "runtime"
    "sync"
)

func main() {
    n := 1000
    data := make([]int, n)
    for i := 0; i < n; i++ { data[i] = i + 1 }
    threads := runtime.NumCPU()
    if threads < 1 { threads = 4 }
    block := n / threads
    var wg sync.WaitGroup
    ch := make(chan int, threads)
    for i := 0; i < threads; i++ {
        s := i * block
        end := (i+1) * block
        if i == threads-1 { end = n }
        wg.Add(1)
        go func(start, end int) {
            defer wg.Done()
            sum := 0
            for j := start; j < end; j++ { sum += data[j] }
            ch <- sum
        }(s, end)
    }
    wg.Wait()
    close(ch)
    total := 0
    for v := range ch { total += v }
    fmt.Println("Total:", total)
}
