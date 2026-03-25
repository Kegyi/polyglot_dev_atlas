class MedianFinder {
    // lo: max-heap (negated), hi: min-heap
    private lo: number[] = [];
    private hi: number[] = [];

    addNum(num: number): void {
        this.heapPush(this.lo, -num, true);
        this.heapPush(this.hi, -this.heapPop(this.lo, true), false);
        if (this.hi.length > this.lo.length) {
            this.heapPush(this.lo, -this.heapPop(this.hi, false), true);
        }
    }

    findMedian(): number {
        if (this.lo.length > this.hi.length) return -this.lo[0];
        return (-this.lo[0] + this.hi[0]) / 2;
    }

    private heapPush(h: number[], val: number, isMax: boolean): void {
        h.push(val);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (isMax ? h[p] >= h[i] : h[p] <= h[i]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    }

    private heapPop(h: number[], isMax: boolean): number {
        const top = h[0];
        const last = h.pop()!;
        if (h.length > 0) {
            h[0] = last;
            let i = 0;
            while (true) {
                let best = i;
                const l = 2 * i + 1, r = 2 * i + 2;
                if (l < h.length && (isMax ? h[l] > h[best] : h[l] < h[best])) best = l;
                if (r < h.length && (isMax ? h[r] > h[best] : h[r] < h[best])) best = r;
                if (best === i) break;
                [h[i], h[best]] = [h[best], h[i]];
                i = best;
            }
        }
        return top;
    }
}
