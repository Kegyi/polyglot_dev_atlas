#include <vector>
#include <unordered_map>
#include <climits>
using namespace std;

class Solution {
public:
    vector<int> shortestSeq(vector<int>& big, vector<int>& small) {
        unordered_map<int, int> need;
        for (int x : small) need[x]++;
        unordered_map<int, int> window;
        int cnt = small.size();
        int j = 0, k = -1, mi = INT_MAX;
        for (int i = 0; i < (int)big.size(); ++i) {
            window[big[i]]++;
            if (need[big[i]] >= window[big[i]]) cnt--;
            while (cnt == 0) {
                if (i - j + 1 < mi) { mi = i - j + 1; k = j; }
                if (need[big[j]] >= window[big[j]]) cnt++;
                window[big[j]]--;
                j++;
            }
        }
        if (k == -1) return {};
        return {k, k + mi - 1};
    }
};
