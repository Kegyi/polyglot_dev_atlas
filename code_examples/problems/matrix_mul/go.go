package main

import "fmt"

func main() {
    const N = 200
    A := make([][]int, N)
    B := make([][]int, N)
    C := make([][]int, N)
    for i := 0; i < N; i++ {
        A[i] = make([]int, N)
        B[i] = make([]int, N)
        C[i] = make([]int, N)
        for j := 0; j < N; j++ {
            A[i][j] = i + j
            B[i][j] = i - j
        }
    }
    for i := 0; i < N; i++ {
        for k := 0; k < N; k++ {
            for j := 0; j < N; j++ {
                C[i][j] += A[i][k] * B[k][j]
            }
        }
    }
    fmt.Println(C[0][0])
}
