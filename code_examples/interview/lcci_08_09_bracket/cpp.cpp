#include <iostream>
#include <vector>
#include <string>
#include <functional>
using namespace std;

vector<string> generateParenthesis(int n) {
    vector<string> result;
    function<void(string, int, int)> bt = [&](string cur, int open, int close) {
        if ((int)cur.size() == 2 * n) { result.push_back(cur); return; }
        if (open < n) bt(cur + "(", open + 1, close);
        if (close < open) bt(cur + ")", open, close + 1);
    };
    bt("", 0, 0);
    return result;
}

int main() {
    for (const auto& s : generateParenthesis(3)) {
        cout << s << endl;
    }
    return 0;
}
