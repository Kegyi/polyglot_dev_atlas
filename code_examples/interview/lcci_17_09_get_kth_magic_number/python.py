class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k + 1)
        dp[1] = 1
        i3 = i5 = i7 = 1
        for i in range(2, k + 1):
            a = dp[i3] * 3
            b = dp[i5] * 5
            c = dp[i7] * 7
            dp[i] = min(a, b, c)
            if dp[i] == a:
                i3 += 1
            if dp[i] == b:
                i5 += 1
            if dp[i] == c:
                i7 += 1
        return dp[k]


def main():
    sol = Solution()
    print(sol.getKthMagicNumber(5))  # 9
    print(sol.getKthMagicNumber(1))  # 1


if __name__ == "__main__":
    main()
