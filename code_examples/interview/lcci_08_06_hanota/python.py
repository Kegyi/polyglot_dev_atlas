from typing import List

def hanota(A: List[int], B: List[int], C: List[int]) -> None:
    def move(n, src, aux, dst):
        if n == 0:
            return
        move(n - 1, src, dst, aux)
        dst.append(src.pop())
        move(n - 1, aux, src, dst)

    move(len(A), A, B, C)

def main():
    A, B, C = [2, 1, 0], [], []
    hanota(A, B, C)
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")

if __name__ == "__main__":
    main()
