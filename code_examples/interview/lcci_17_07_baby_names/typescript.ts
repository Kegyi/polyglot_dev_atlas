function trulyMostPopular(names: string[], synonyms: string[]): string[] {
    const parent = new Map<string, string>();

    const find = (x: string): string => {
        if (!parent.has(x)) parent.set(x, x);
        if (parent.get(x)! !== x) parent.set(x, find(parent.get(x)!));
        return parent.get(x)!;
    };

    const unite = (a: string, b: string): void => {
        const pa = find(a);
        const pb = find(b);
        if (pa !== pb) {
            if (pa < pb) parent.set(pb, pa);
            else parent.set(pa, pb);
        }
    };

    const freq = new Map<string, number>();
    for (const s of names) {
        const idx = s.indexOf('(');
        const name = s.slice(0, idx);
        const count = Number(s.slice(idx + 1, -1));
        freq.set(name, count);
    }

    for (const syn of synonyms) {
        const s = syn.slice(1, -1);
        const comma = s.indexOf(',');
        unite(s.slice(0, comma), s.slice(comma + 1));
    }

    const result = new Map<string, number>();
    for (const [name, cnt] of freq) {
        const root = find(name);
        result.set(root, (result.get(root) ?? 0) + cnt);
    }

    return [...result.entries()]
        .sort((a, b) => a[0].localeCompare(b[0]))
        .map(([name, cnt]) => `${name}(${cnt})`);
}

const names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"];
const synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"];
console.log(trulyMostPopular(names, synonyms).join(' ')); // Chris(36) John(27)
