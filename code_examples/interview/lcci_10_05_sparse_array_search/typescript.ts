function findString(words: string[], target: string): number {
    let left = 0;
    let right = words.length - 1;
    let answer = -1;
    while (left <= right) {
        const mid = (left + right) >> 1;
        let lo = mid;
        let hi = mid;
        let actual = -1;
        while (lo >= left || hi <= right) {
            if (lo >= left && words[lo] !== "") {
                actual = lo;
                break;
            }
            if (hi <= right && words[hi] !== "") {
                actual = hi;
                break;
            }
            lo -= 1;
            hi += 1;
        }
        if (actual === -1) {
            break;
        }
        if (words[actual] === target) {
            answer = actual;
            right = actual - 1;
        } else if (words[actual] < target) {
            left = actual + 1;
        } else {
            right = actual - 1;
        }
    }
    return answer;
}

const words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""];
console.log(findString(words, "ta"));
console.log(findString(words, "ball"));
