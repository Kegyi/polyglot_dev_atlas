const ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
const TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
const TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
const UNITS = ["", "Thousand", "Million", "Billion"];

function below1000(n: number): string {
    const parts: string[] = [];
    if (n >= 100) {
        parts.push(ONES[Math.floor(n / 100)]);
        parts.push("Hundred");
        n %= 100;
    }
    if (n >= 20) {
        parts.push(TENS[Math.floor(n / 10)]);
        if (n % 10) parts.push(ONES[n % 10]);
    } else if (n >= 10) {
        parts.push(TEENS[n - 10]);
    } else if (n > 0) {
        parts.push(ONES[n]);
    }
    return parts.join(" ");
}

function numberToWords(num: number): string {
    if (num === 0) return "Zero";
    if (num < 0) return "Negative " + numberToWords(-num);

    const parts: string[] = [];
    let unit = 0;
    while (num > 0) {
        const chunk = num % 1000;
        if (chunk > 0) {
            let piece = below1000(chunk);
            if (UNITS[unit] !== "") piece += " " + UNITS[unit];
            parts.push(piece);
        }
        num = Math.floor(num / 1000);
        unit += 1;
    }
    return parts.reverse().join(" ");
}

console.log(numberToWords(123));
console.log(numberToWords(12345));
console.log(numberToWords(-1000010));
