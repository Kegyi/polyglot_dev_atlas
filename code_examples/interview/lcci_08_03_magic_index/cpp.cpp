#include <iostream>
#include <vector>
using namespace std;

int findMagicIndex(vector<int>& nums) {
    int lo = 0, hi = (int)nums.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == mid) return mid;
        if (nums[mid] < mid) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> a = {-1, 1, 3, 4, 6};
    cout << findMagicIndex(a) << endl; // 1
    vector<int> b = {0, 2, 3, 4, 5};
    cout << findMagicIndex(b) << endl; // 0
    return 0;
}
