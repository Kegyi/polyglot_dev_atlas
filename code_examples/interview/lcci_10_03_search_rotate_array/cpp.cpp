#include <iostream>
#include <vector>
using namespace std;

int search(const vector<int>& arr, int target) {
    if (arr.empty()) {
        return -1;
    }
    int left = 0;
    int right = static_cast<int>(arr.size()) - 1;
    while (left < right && arr[left] == arr[right]) {
        --right;
    }
    while (left < right) {
        int mid = (left + right) >> 1;
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
            --right;
        }
    }
    return arr[left] == target ? left : -1;
}

int main() {
    vector<int> arr = {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14};
    cout << search(arr, 5) << endl;
    cout << search(arr, 11) << endl;
    return 0;
}
