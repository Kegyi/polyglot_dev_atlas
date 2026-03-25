#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<vector<string>> groupAnagrams(const vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    for (const string& s : strs) {
        string key = s;
        sort(key.begin(), key.end());
        groups[key].push_back(s);
    }

    vector<vector<string>> result;
    for (auto& entry : groups) {
        sort(entry.second.begin(), entry.second.end());
        result.push_back(entry.second);
    }
    sort(result.begin(), result.end(), [](const vector<string>& a, const vector<string>& b) {
        return a[0] < b[0];
    });
    return result;
}

int main() {
    vector<vector<string>> groups = groupAnagrams({"eat", "tea", "tan", "ate", "nat", "bat"});
    cout << "[";
    for (int i = 0; i < static_cast<int>(groups.size()); ++i) {
        if (i) cout << ", ";
        cout << "[";
        for (int j = 0; j < static_cast<int>(groups[i].size()); ++j) {
            if (j) cout << ", ";
            cout << groups[i][j];
        }
        cout << "]";
    }
    cout << "]" << endl;
    return 0;
}
