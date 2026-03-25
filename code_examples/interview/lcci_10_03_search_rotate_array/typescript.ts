function search(arr: number[], target: number): number {
    if (arr.length === 0) {
        return -1;
    }
    let left = 0;
    let right = arr.length - 1;
    while (left < right && arr[left] === arr[right]) {
        right -= 1;
    }
    while (left < right) {
        const mid = (left + right) >> 1;
        if (arr[mid] > arr[right]) {
            if (arr[left] <= target && target <= arr[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        } else if (arr[mid] < arr[right]) {
            if (arr[mid] < target && target <= arr[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        } else {
            right -= 1;
        }
    }
    return arr[left] === target ? left : -1;
}

const arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14];
console.log(search(arr, 5));
console.log(search(arr, 11));
