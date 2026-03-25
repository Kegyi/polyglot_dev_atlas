#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
        vector<pair<int, int>> people;
        for (int i = 0; i < (int)height.size(); i++) {
            people.push_back({height[i], weight[i]});
        }
        sort(people.begin(), people.end(), [](const auto& a, const auto& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second;
        });

        vector<int> lis;
        for (auto& p : people) {
            int w = p.second;
            auto it = lower_bound(lis.begin(), lis.end(), w);
            if (it == lis.end()) lis.push_back(w);
            else *it = w;
        }
        return (int)lis.size();
    }
};

int main() {
    Solution sol;
    vector<int> h1 = {65, 70, 56, 75, 60, 68};
    vector<int> w1 = {100, 150, 90, 190, 95, 110};
    cout << sol.bestSeqAtIndex(h1, w1) << endl; // 6

    vector<int> h2 = {65, 70, 56, 75};
    vector<int> w2 = {100, 150, 90, 190};
    cout << sol.bestSeqAtIndex(h2, w2) << endl; // 4
    return 0;
}
