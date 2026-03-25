package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
    "sync"
    "sort"
)

type Record struct {
    Name  string
    Score int
}

func readAll(path string) ([]Record, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close()
    var out []Record
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        line := strings.TrimSpace(scanner.Text())
        if line == "" || strings.HasPrefix(line, "#") {
            continue
        }
        parts := strings.SplitN(line, ",", 2)
        if len(parts) != 2 {
            continue
        }
        name := strings.TrimSpace(parts[0])
        s := strings.TrimSpace(parts[1])
        score, err := strconv.Atoi(s)
        if err != nil {
            continue
        }
        out = append(out, Record{name, score})
    }
    if err := scanner.Err(); err != nil {
        return nil, err
    }
    return out, nil
}

func average(nums []int) float64 {
    if len(nums) == 0 {
        return 0
    }
    sum := 0
    for _, v := range nums {
        sum += v
    }
    return float64(sum) / float64(len(nums))
}

func main() {
    path := "data.txt"
    if len(os.Args) > 1 {
        path = os.Args[1]
    }
    records, err := readAll(path)
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(1)
    }

    buckets := map[string][]int{}
    for _, r := range records {
        buckets[r.Name] = append(buckets[r.Name], r.Score)
    }

    type Res struct {
        Name string
        Avg  float64
    }

    var wg sync.WaitGroup
    ch := make(chan Res, len(buckets))
    for name, scores := range buckets {
        wg.Add(1)
        go func(n string, s []int) {
            defer wg.Done()
            ch <- Res{n, average(s)}
        }(name, scores)
    }
    wg.Wait()
    close(ch)

    var results []Res
    for r := range ch {
        results = append(results, r)
    }

    sort.Slice(results, func(i, j int) bool { return results[i].Avg > results[j].Avg })
    for _, r := range results {
        fmt.Printf("%s: %.2f\n", r.Name, r.Avg)
    }
}
