#include <string>
#include <vector>
using namespace std;

struct Trie {
    Trie* children[26] = {};
    int idx = -1;

    void insert(const string& word, int i) {
        Trie* node = this;
        for (char c : word) {
            int j = c - 'a';
            if (!node->children[j]) node->children[j] = new Trie();
            node = node->children[j];
        }
        node->idx = i;
    }
};

class Solution {
public:
    vector<vector<int>> multiSearch(string big, vector<string>& smalls) {
        Trie* trie = new Trie();
        for (int i = 0; i < (int)smalls.size(); ++i) {
            if (!smalls[i].empty()) trie->insert(smalls[i], i);
        }
        int n = big.size();
        vector<vector<int>> ans(smalls.size());
        for (int i = 0; i < n; ++i) {
            Trie* node = trie;
            for (int j = i; j < n; ++j) {
                int k = big[j] - 'a';
                if (!node->children[k]) break;
                node = node->children[k];
                if (node->idx != -1) ans[node->idx].push_back(i);
            }
        }
        return ans;
    }
};
