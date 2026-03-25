#include <iostream>
#include <vector>
using namespace std;

vector<int> divingBoard(int shorter, int longer, int k) {
    if (k == 0) return {};
    if (shorter == longer) return {shorter * k};
    vector<int> ans;
    for (int i = 0; i <= k; ++i) {
        ans.push_back(shorter * (k - i) + longer * i);
    }
    return ans;
}

int main() {
    vector<int> ans = divingBoard(1, 2, 3);
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << ans[i];
    }
    cout << "]" << endl;
    return 0;
}
