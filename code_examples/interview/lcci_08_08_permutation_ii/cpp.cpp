#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> permutation(string S) {
    sort(S.begin(), S.end());
    vector<string> result;
    do {
        result.push_back(S);
    } while (next_permutation(S.begin(), S.end()));
    return result;
}

int main() {
    for (const auto& p : permutation("qqe")) {
        cout << p << endl;
    }
    return 0;
}
