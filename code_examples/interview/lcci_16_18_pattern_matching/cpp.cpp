#include <iostream>
#include <string>
using namespace std;

bool patternMatching(const string& pattern, const string& value) {
    if (pattern.empty()) return value.empty();

    int countA = 0, countB = 0;
    for (char ch : pattern) {
        if (ch == 'a') ++countA;
        else ++countB;
    }

    if (countA < countB) {
        string swapped = pattern;
        for (char& ch : swapped) ch = (ch == 'a' ? 'b' : 'a');
        return patternMatching(swapped, value);
    }

    if (value.empty()) return countB == 0;

    int n = value.size();
    for (int lenA = 0; countA * lenA <= n; ++lenA) {
        int rest = n - countA * lenA;
        if (countB == 0) {
            if (rest != 0) continue;
        } else if (rest % countB != 0) {
            continue;
        }
        int lenB = (countB == 0 ? 0 : rest / countB);

        int pos = 0;
        string a = "#", b = "#";
        bool ok = true;
        for (char ch : pattern) {
            if (ch == 'a') {
                string sub = value.substr(pos, lenA);
                if (a == "#") a = sub;
                else if (a != sub) { ok = false; break; }
                pos += lenA;
            } else {
                string sub = value.substr(pos, lenB);
                if (b == "#") b = sub;
                else if (b != sub) { ok = false; break; }
                pos += lenB;
            }
        }
        if (ok && a != b) return true;
    }
    return false;
}

int main() {
    cout << boolalpha << patternMatching("abba", "dogcatcatdog") << endl;
    cout << boolalpha << patternMatching("abba", "dogcatcatfish") << endl;
    return 0;
}
