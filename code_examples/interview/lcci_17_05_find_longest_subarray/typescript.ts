function findLongestSubarray(array: string[]): string[] {
    const first = new Map<number, number>();
    first.set(0, -1);
    let s = 0, maxLen = 0, start = 0;
    for (let i = 0; i < array.length; i++) {
        s += /[a-zA-Z]/.test(array[i]) ? 1 : -1;
        if (first.has(s)) {
            const length = i - first.get(s)!;
            if (length > maxLen) {
                maxLen = length;
                start = first.get(s)! + 1;
            }
        } else {
            first.set(s, i);
        }
    }
    return array.slice(start, start + maxLen);
}

const arr1 = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"];
console.log(findLongestSubarray(arr1).join(' ')); // A 1 B C D 2 3 4 E 5 F G 6 7

const arr2 = ["A", "A"];
const res2 = findLongestSubarray(arr2);
console.log(res2.length === 0 ? "(empty)" : res2.join(' '));
