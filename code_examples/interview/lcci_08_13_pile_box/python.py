from typing import List

def pileBox(box: List[List[int]]) -> int:
    box.sort(key=lambda b: (-b[0], -b[1]))
    n = len(box)
    dp = [b[2] for b in box]
    ans = max(dp)
    for i in range(1, n):
        for j in range(i):
            if box[j][0] > box[i][0] and box[j][1] > box[i][1] and box[j][2] > box[i][2]:
                dp[i] = max(dp[i], dp[j] + box[i][2])
        ans = max(ans, dp[i])
    return ans

def main():
    print(pileBox([[2,2,2],[3,3,3],[4,4,4]]))  # 9

if __name__ == "__main__":
    main()
