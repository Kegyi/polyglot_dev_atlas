class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        count = 0
        m = 1
        while m <= n:
            a, b = n // m, n % m
            digit = a % 10
            if digit > 2:
                count += (a // 10 + 1) * m
            elif digit == 2:
                count += (a // 10) * m + b + 1
            else:
                count += (a // 10) * m
            m *= 10
        return count


def main():
    sol = Solution()
    print(sol.numberOf2sInRange(25))  # 9
    print(sol.numberOf2sInRange(20))  # 2


if __name__ == "__main__":
    main()
