function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();
    for (const word of strs) {
        const key = [...word].sort().join("");
        const group = groups.get(key) ?? [];
        group.push(word);
        groups.set(key, group);
    }
    const result = [...groups.values()].map((group) => group.sort());
    result.sort((a, b) => a[0].localeCompare(b[0]));
    return result;
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
