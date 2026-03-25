class Operations {
    minus(a: number, b: number): number {
        return a - b;
    }

    multiply(a: number, b: number): number {
        return a * b;
    }

    divide(a: number, b: number): number {
        return Math.trunc(a / b);
    }
}

const ops = new Operations();
console.log(ops.minus(10, 3));
console.log(ops.multiply(6, -4));
console.log(ops.divide(20, 5));
