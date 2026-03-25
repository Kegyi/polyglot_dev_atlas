def waysToChange(n: int) -> int:
    MOD = 10**9 + 7
    coins = [1, 5, 10, 25]
    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i - coin]) % MOD
    return dp[n]

def main():
    print(waysToChange(5))   # 2
    print(waysToChange(10))  # 4

if __name__ == "__main__":
    main()
