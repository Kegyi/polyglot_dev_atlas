class TrieNode {
    children: (TrieNode | null)[] = new Array(26).fill(null);
    idx: number = -1;
}

function multiSearch(big: string, smalls: string[]): number[][] {
    const root = new TrieNode();
    const insert = (word: string, i: number) => {
        let node = root;
        for (const c of word) {
            const j = c.charCodeAt(0) - 97;
            if (!node.children[j]) node.children[j] = new TrieNode();
            node = node.children[j]!;
        }
        node.idx = i;
    };
    for (let i = 0; i < smalls.length; i++) {
        if (smalls[i]) insert(smalls[i], i);
    }
    const ans: number[][] = smalls.map(() => []);
    for (let i = 0; i < big.length; i++) {
        let node = root;
        for (let j = i; j < big.length; j++) {
            const k = big.charCodeAt(j) - 97;
            if (!node.children[k]) break;
            node = node.children[k]!;
            if (node.idx !== -1) ans[node.idx].push(i);
        }
    }
    return ans;
}
