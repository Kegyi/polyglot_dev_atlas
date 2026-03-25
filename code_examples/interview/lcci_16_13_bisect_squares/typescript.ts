function cutSquares(square1: number[], square2: number[]): number[] {
    const [x1, y1, s1] = square1;
    const [x2, y2, s2] = square2;

    const cx1 = x1 + s1 / 2;
    const cy1 = y1 + s1 / 2;
    const cx2 = x2 + s2 / 2;
    const cy2 = y2 + s2 / 2;

    if (Math.abs(cx1 - cx2) < 1e-9) {
        const x = cx1;
        const yBottom = Math.min(y1, y2);
        const yTop = Math.max(y1 + s1, y2 + s2);
        return [x, yBottom, x, yTop];
    }

    const k = (cy2 - cy1) / (cx2 - cx1);
    const b = cy1 - k * cx1;

    let px1: number;
    let py1: number;
    let px2: number;
    let py2: number;

    if (Math.abs(k) <= 1) {
        px1 = Math.min(x1, x2);
        px2 = Math.max(x1 + s1, x2 + s2);
        py1 = k * px1 + b;
        py2 = k * px2 + b;
    } else {
        py1 = Math.min(y1, y2);
        py2 = Math.max(y1 + s1, y2 + s2);
        px1 = (py1 - b) / k;
        px2 = (py2 - b) / k;
    }

    if (px1 > px2 || (Math.abs(px1 - px2) < 1e-9 && py1 > py2)) {
        [px1, px2] = [px2, px1];
        [py1, py2] = [py2, py1];
    }

    return [px1, py1, px2, py2];
}

console.log(cutSquares([-1, -1, 2], [0, -1, 2]));
