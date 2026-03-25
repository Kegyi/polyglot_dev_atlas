#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<string> findLongestSubarray(vector<string>& array) {
        unordered_map<int, int> first;
        first[0] = -1;
        int s = 0, maxLen = 0, start = 0;
        for (int i = 0; i < (int)array.size(); i++) {
            s += isalpha(array[i][0]) ? 1 : -1;
            if (first.count(s)) {
                int len = i - first[s];
                if (len > maxLen) {
                    maxLen = len;
                    start = first[s] + 1;
                }
            } else {
                first[s] = i;
            }
        }
        return vector<string>(array.begin() + start, array.begin() + start + maxLen);
    }
};

int main() {
    Solution sol;
    vector<string> arr1 = {"A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"};
    auto res1 = sol.findLongestSubarray(arr1);
    for (auto& s : res1) cout << s << " ";
    cout << endl;

    vector<string> arr2 = {"A","A"};
    auto res2 = sol.findLongestSubarray(arr2);
    if (res2.empty()) cout << "(empty)" << endl;
    return 0;
}
