function collinear(a: number[], b: number[], c: number[]): boolean {
    const x1 = b[0] - a[0];
    const y1 = b[1] - a[1];
    const x2 = c[0] - a[0];
    const y2 = c[1] - a[1];
    return x1 * y2 === x2 * y1;
}

function bestLine(points: number[][]): number[] {
    const n = points.length;
    let bestI = 0;
    let bestJ = 1;
    let bestCount = 2;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let count = 2;
            for (let k = j + 1; k < n; k++) {
                if (collinear(points[i], points[j], points[k])) {
                    count += 1;
                }
            }
            if (count > bestCount || (count === bestCount && (i < bestI || (i === bestI && j < bestJ)))) {
                bestI = i;
                bestJ = j;
                bestCount = count;
            }
        }
    }
    return [bestI, bestJ];
}

console.log(bestLine([[0, 0], [1, 1], [1, 0], [2, 2]]));
