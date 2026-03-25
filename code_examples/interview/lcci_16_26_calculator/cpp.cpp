#include <iostream>
#include <string>
#include <vector>
using namespace std;

int calculate(const string& s) {
    vector<int> st;
    int n = s.size();
    long long num = 0;
    char op = '+';
    for (int i = 0; i <= n; ++i) {
        char ch = (i < n ? s[i] : '+');
        if (ch == ' ') continue;
        if (isdigit(ch)) {
            num = num * 10 + (ch - '0');
            continue;
        }
        if (op == '+') st.push_back(static_cast<int>(num));
        else if (op == '-') st.push_back(static_cast<int>(-num));
        else if (op == '*') {
            int v = st.back(); st.pop_back();
            st.push_back(v * static_cast<int>(num));
        } else {
            int v = st.back(); st.pop_back();
            st.push_back(v / static_cast<int>(num));
        }
        op = ch;
        num = 0;
    }
    int ans = 0;
    for (int v : st) ans += v;
    return ans;
}

int main() {
    cout << calculate("3+2*2") << endl;
    cout << calculate(" 3/2 ") << endl;
    cout << calculate(" 3+5 / 2 ") << endl;
    return 0;
}
