const EPS = 1e-9;

function lessPoint(a: number[], b: number[]): boolean {
    if (Math.abs(a[0] - b[0]) > EPS) {
        return a[0] < b[0];
    }
    return a[1] < b[1] - EPS;
}

function cross(a: number[], b: number[], c: number[]): number {
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
}

function onSegment(a: number[], b: number[], p: number[]): boolean {
    return Math.abs(cross(a, b, p)) < EPS &&
        Math.min(a[0], b[0]) - EPS <= p[0] && p[0] <= Math.max(a[0], b[0]) + EPS &&
        Math.min(a[1], b[1]) - EPS <= p[1] && p[1] <= Math.max(a[1], b[1]) + EPS;
}

function intersection(start1: number[], end1: number[], start2: number[], end2: number[]): number[] {
    if (lessPoint(end1, start1)) {
        [start1, end1] = [end1, start1];
    }
    if (lessPoint(end2, start2)) {
        [start2, end2] = [end2, start2];
    }

    const d1 = cross(start1, end1, start2);
    const d2 = cross(start1, end1, end2);
    const d3 = cross(start2, end2, start1);
    const d4 = cross(start2, end2, end1);

    if (((d1 > EPS && d2 > EPS) || (d1 < -EPS && d2 < -EPS)) ||
        ((d3 > EPS && d4 > EPS) || (d3 < -EPS && d4 < -EPS))) {
        return [];
    }

    const a1 = end1[1] - start1[1];
    const b1 = start1[0] - end1[0];
    const c1 = a1 * start1[0] + b1 * start1[1];

    const a2 = end2[1] - start2[1];
    const b2 = start2[0] - end2[0];
    const c2 = a2 * start2[0] + b2 * start2[1];

    const det = a1 * b2 - a2 * b1;
    if (Math.abs(det) < EPS) {
        const candidates: number[][] = [];
        if (onSegment(start1, end1, start2)) candidates.push(start2);
        if (onSegment(start1, end1, end2)) candidates.push(end2);
        if (onSegment(start2, end2, start1)) candidates.push(start1);
        if (onSegment(start2, end2, end1)) candidates.push(end1);
        if (candidates.length === 0) return [];
        candidates.sort((p, q) => p[0] !== q[0] ? p[0] - q[0] : p[1] - q[1]);
        return candidates[0];
    }

    const x = (b2 * c1 - b1 * c2) / det;
    const y = (a1 * c2 - a2 * c1) / det;
    const p = [x, y];
    return onSegment(start1, end1, p) && onSegment(start2, end2, p) ? p : [];
}

console.log(intersection([0, 0], [1, 0], [1, 1], [0, -1]));
