#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
    unordered_set<string> wordSet;

    bool canBuild(const string& w) {
        if (w.empty()) return true;
        for (int i = 1; i <= (int)w.size(); ++i) {
            if (wordSet.count(w.substr(0, i)) && canBuild(w.substr(i))) {
                return true;
            }
        }
        return false;
    }

public:
    string longestWord(vector<string>& words) {
        for (auto& w : words) wordSet.insert(w);
        sort(words.begin(), words.end(), [](const string& a, const string& b) {
            return a.size() != b.size() ? a.size() > b.size() : a < b;
        });
        for (auto& w : words) {
            wordSet.erase(w);
            if (canBuild(w)) return w;
            wordSet.insert(w);
        }
        return "";
    }
};
