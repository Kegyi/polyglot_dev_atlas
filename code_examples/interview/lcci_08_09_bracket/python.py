from typing import List

def generateParenthesis(n: int) -> List[str]:
    result = []

    def bt(cur, open_count, close_count):
        if len(cur) == 2 * n:
            result.append(cur)
            return
        if open_count < n:
            bt(cur + "(", open_count + 1, close_count)
        if close_count < open_count:
            bt(cur + ")", open_count, close_count + 1)

    bt("", 0, 0)
    return result

def main():
    for s in generateParenthesis(3):
        print(s)

if __name__ == "__main__":
    main()
