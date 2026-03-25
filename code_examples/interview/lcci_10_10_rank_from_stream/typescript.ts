class BinaryIndexedTree {
    private readonly tree: number[];

    constructor(size: number) {
        this.tree = new Array(size + 1).fill(0);
    }

    update(index: number, delta: number): void {
        while (index < this.tree.length) {
            this.tree[index] += delta;
            index += index & -index;
        }
    }

    query(index: number): number {
        let sum = 0;
        while (index > 0) {
            sum += this.tree[index];
            index -= index & -index;
        }
        return sum;
    }
}

class StreamRank {
    private readonly bit = new BinaryIndexedTree(50010);

    track(x: number): void {
        this.bit.update(x + 1, 1);
    }

    getRankOfNumber(x: number): number {
        return this.bit.query(x + 1);
    }
}

const streamRank = new StreamRank();
console.log(streamRank.getRankOfNumber(1));
streamRank.track(0);
console.log(streamRank.getRankOfNumber(0));
