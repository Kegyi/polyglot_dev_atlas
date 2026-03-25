#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
    unordered_map<string, string> parent;

    string find(const string& x) {
        if (parent.find(x) == parent.end()) parent[x] = x;
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(const string& a, const string& b) {
        string pa = find(a), pb = find(b);
        if (pa != pb) {
            if (pa < pb) parent[pb] = pa;
            else parent[pa] = pb;
        }
    }

public:
    vector<string> trulyMostPopular(vector<string>& names, vector<string>& synonyms) {
        unordered_map<string, int> freq;
        for (auto& s : names) {
            size_t paren = s.find('(');
            string name = s.substr(0, paren);
            int count = stoi(s.substr(paren + 1, s.size() - paren - 2));
            freq[name] = count;
        }
        for (auto& syn : synonyms) {
            string s = syn.substr(1, syn.size() - 2);
            size_t comma = s.find(',');
            unite(s.substr(0, comma), s.substr(comma + 1));
        }
        unordered_map<string, int> result;
        for (auto& [name, cnt] : freq) {
            result[find(name)] += cnt;
        }
        vector<string> ans;
        for (auto& [name, cnt] : result) {
            ans.push_back(name + "(" + to_string(cnt) + ")");
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};

int main() {
    Solution sol;
    vector<string> names = {"John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"};
    vector<string> synonyms = {"(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"};
    auto res = sol.trulyMostPopular(names, synonyms);
    for (auto& s : res) cout << s << " ";
    cout << endl;
    return 0;
}
