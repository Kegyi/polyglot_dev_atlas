#include <iostream>
#include <vector>
#include <string>
#include <climits>
using namespace std;

class Solution {
public:
    int findClosest(vector<string>& words, string word1, string word2) {
        int i1 = -1, i2 = -1, ans = INT_MAX;
        for (int i = 0; i < (int)words.size(); i++) {
            if (words[i] == word1) i1 = i;
            if (words[i] == word2) i2 = i;
            if (i1 != -1 && i2 != -1) ans = min(ans, abs(i1 - i2));
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<string> w1 = {"I","am","a","student","from","a","university","in","a","city"};
    cout << sol.findClosest(w1, "a", "student") << endl; // 1

    vector<string> w2 = {"aa", "bb"};
    cout << sol.findClosest(w2, "aa", "bb") << endl; // 1
    return 0;
}
