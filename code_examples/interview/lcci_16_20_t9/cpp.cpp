#include <iostream>
#include <string>
#include <vector>
using namespace std;

char mapDigit(char ch) {
    if (ch <= 'c') return '2';
    if (ch <= 'f') return '3';
    if (ch <= 'i') return '4';
    if (ch <= 'l') return '5';
    if (ch <= 'o') return '6';
    if (ch <= 's') return '7';
    if (ch <= 'v') return '8';
    return '9';
}

vector<string> getValidT9Words(const string& num, const vector<string>& words) {
    vector<string> ans;
    for (const string& word : words) {
        if (word.size() != num.size()) continue;
        bool ok = true;
        for (int i = 0; i < static_cast<int>(word.size()); ++i) {
            if (mapDigit(word[i]) != num[i]) {
                ok = false;
                break;
            }
        }
        if (ok) ans.push_back(word);
    }
    return ans;
}

int main() {
    vector<string> ans = getValidT9Words("8733", {"tree", "used", "true"});
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << ans[i];
    }
    cout << "]" << endl;
    return 0;
}
