ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
UNITS = ["", "Thousand", "Million", "Billion"]


def below_1000(n: int) -> str:
    parts = []
    if n >= 100:
        parts.append(ONES[n // 100])
        parts.append("Hundred")
        n %= 100
    if n >= 20:
        parts.append(TENS[n // 10])
        if n % 10:
            parts.append(ONES[n % 10])
    elif n >= 10:
        parts.append(TEENS[n - 10])
    elif n > 0:
        parts.append(ONES[n])
    return " ".join(parts)


def number_to_words(num: int) -> str:
    if num == 0:
        return "Zero"
    if num < 0:
        return "Negative " + number_to_words(-num)

    parts = []
    unit = 0
    while num > 0:
        chunk = num % 1000
        if chunk:
            piece = below_1000(chunk)
            if UNITS[unit]:
                piece += f" {UNITS[unit]}"
            parts.append(piece)
        num //= 1000
        unit += 1
    return " ".join(reversed(parts))


def main() -> None:
    print(number_to_words(123))
    print(number_to_words(12345))
    print(number_to_words(-1000010))


if __name__ == "__main__":
    main()
