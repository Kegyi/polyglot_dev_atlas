def draw_line(length: int, w: int, x1: int, x2: int, y: int) -> list[int]:
    words_per_row = w // 32
    screen = [0] * length
    offset = y * words_per_row

    start_word = x1 // 32 + offset
    end_word   = x2 // 32 + offset
    start_bit  = x1 % 32
    end_bit    = x2 % 32

    for i in range(start_word, end_word + 1):
        hi = (0xFF >> start_bit) if i == start_word else 0xFF
        lo = (~(0xFF >> (end_bit + 1))) & 0xFF if i == end_word else 0xFF
        screen[i] = hi & lo

    return screen


def main() -> None:
    result = draw_line(1, 32, 1, 30, 0)
    for v in result:
        print(hex(v))


if __name__ == "__main__":
    main()
