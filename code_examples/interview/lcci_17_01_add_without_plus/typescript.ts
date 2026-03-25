function add(a: number, b: number): number {
    while (b !== 0) {
        const carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}

console.log(add(1, 2));    // 3
console.log(add(3, -2));   // 1
console.log(add(-1, -2));  // -3
