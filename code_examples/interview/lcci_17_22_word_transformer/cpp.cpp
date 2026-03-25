#include <string>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
public:
    vector<string> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) return {};

        queue<vector<string>> q;
        q.push({beginWord});
        unordered_set<string> visited = {beginWord};

        while (!q.empty()) {
            auto path = q.front(); q.pop();
            string cur = path.back();
            for (int i = 0; i < (int)cur.size(); ++i) {
                char orig = cur[i];
                for (char c = 'a'; c <= 'z'; ++c) {
                    if (c == orig) continue;
                    cur[i] = c;
                    auto newPath = path;
                    newPath.push_back(cur);
                    if (cur == endWord) return newPath;
                    if (wordSet.count(cur) && !visited.count(cur)) {
                        visited.insert(cur);
                        q.push(newPath);
                    }
                    cur[i] = orig;
                }
            }
        }
        return {};
    }
};
