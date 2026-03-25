def waysToStep(n: int) -> int:
    MOD = 10**9 + 7
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    a, b, c = 1, 2, 4
    for _ in range(n - 3):
        a, b, c = b, c, (a + b + c) % MOD
    return c

def main():
    print(waysToStep(3))  # 4
    print(waysToStep(5))  # 13

if __name__ == "__main__":
    main()
