#include <iostream>
#include <vector>
#include <numeric>

int main() {
    const int N = 200;
    std::vector<std::vector<int>> A(N, std::vector<int>(N)), B(N, std::vector<int>(N)), C(N, std::vector<int>(N, 0));
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) {
            A[i][j] = i + j;
            B[i][j] = i - j;
        }
    for (int i = 0; i < N; ++i)
        for (int k = 0; k < N; ++k)
            for (int j = 0; j < N; ++j)
                C[i][j] += A[i][k] * B[k][j];
    std::cout << C[0][0] << std::endl;
    return 0;
}
