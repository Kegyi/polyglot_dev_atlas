function patternMatching(pattern: string, value: string): boolean {
    if (pattern.length === 0) return value.length === 0;

    let countA = 0;
    let countB = 0;
    for (const ch of pattern) {
        if (ch === "a") countA += 1;
        else countB += 1;
    }

    if (countA < countB) {
        const swapped = [...pattern].map((ch) => (ch === "a" ? "b" : "a")).join("");
        return patternMatching(swapped, value);
    }

    if (value.length === 0) return countB === 0;

    const n = value.length;
    for (let lenA = 0; countA * lenA <= n; lenA++) {
        const rest = n - countA * lenA;
        let lenB = 0;
        if (countB === 0) {
            if (rest !== 0) continue;
        } else {
            if (rest % countB !== 0) continue;
            lenB = rest / countB;
        }

        let pos = 0;
        let a: string | null = null;
        let b: string | null = null;
        let ok = true;
        for (const ch of pattern) {
            if (ch === "a") {
                const sub = value.slice(pos, pos + lenA);
                if (a === null) a = sub;
                else if (a !== sub) {
                    ok = false;
                    break;
                }
                pos += lenA;
            } else {
                const sub = value.slice(pos, pos + lenB);
                if (b === null) b = sub;
                else if (b !== sub) {
                    ok = false;
                    break;
                }
                pos += lenB;
            }
        }
        if (ok && a !== b) return true;
    }
    return false;
}

console.log(patternMatching("abba", "dogcatcatdog"));
console.log(patternMatching("abba", "dogcatcatfish"));
