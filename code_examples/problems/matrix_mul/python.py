def make_matrix(n, init):
    return [[init(i, j) for j in range(n)] for i in range(n)]


def main():
    N = 200
    A = make_matrix(N, lambda i, j: i + j)
    B = make_matrix(N, lambda i, j: i - j)
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            aik = A[i][k]
            for j in range(N):
                C[i][j] += aik * B[k][j]
    print(C[0][0])


if __name__ == '__main__':
    main()
