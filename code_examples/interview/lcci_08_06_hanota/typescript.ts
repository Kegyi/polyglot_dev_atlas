function hanota(A: number[], B: number[], C: number[]): void {
    function move(n: number, src: number[], aux: number[], dst: number[]): void {
        if (n === 0) return;
        move(n - 1, src, dst, aux);
        dst.push(src.pop()!);
        move(n - 1, aux, src, dst);
    }
    move(A.length, A, B, C);
}

const A = [2, 1, 0], B: number[] = [], C: number[] = [];
hanota(A, B, C);
console.log("A:", A);
console.log("B:", B);
console.log("C:", C);
