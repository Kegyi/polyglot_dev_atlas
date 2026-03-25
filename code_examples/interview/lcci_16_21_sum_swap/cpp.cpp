#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> findSwapValues(const vector<int>& array1, const vector<int>& array2) {
    long long sum1 = 0, sum2 = 0;
    for (int x : array1) sum1 += x;
    for (int x : array2) sum2 += x;

    long long diff = sum1 - sum2;
    if (diff % 2 != 0) return {};
    long long target = diff / 2;

    unordered_set<long long> set2;
    for (int y : array2) set2.insert(y);

    for (int x : array1) {
        long long y = x - target;
        if (set2.count(y)) return {x, static_cast<int>(y)};
    }
    return {};
}

int main() {
    vector<int> ans = findSwapValues({4, 1, 2, 1, 1, 2}, {3, 6, 3, 3});
    if (ans.empty()) cout << "[]" << endl;
    else cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
