#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void wiggleSort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i + 1 < static_cast<int>(nums.size()); i += 2) {
        swap(nums[i], nums[i + 1]);
    }
}

int main() {
    vector<int> nums = {5, 3, 1, 2, 3};
    wiggleSort(nums);
    cout << "[";
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        if (i) cout << ", ";
        cout << nums[i];
    }
    cout << "]" << endl;
    return 0;
}
