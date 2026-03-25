class Solution:
    def add(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            carry = ((a & b) & mask) << 1
            a = (a ^ b) & mask
            b = carry
        return a if b == 0 else a | ~mask


def main():
    sol = Solution()
    print(sol.add(1, 2))    # 3
    print(sol.add(3, -2))   # 1
    print(sol.add(-1, -2))  # -3


if __name__ == "__main__":
    main()
