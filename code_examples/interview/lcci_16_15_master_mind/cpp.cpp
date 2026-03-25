#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> masterMind(const string& solution, const string& guess) {
    int hits = 0;
    vector<int> cs(26, 0), cg(26, 0);
    for (int i = 0; i < 4; ++i) {
        if (solution[i] == guess[i]) {
            ++hits;
        } else {
            ++cs[solution[i] - 'A'];
            ++cg[guess[i] - 'A'];
        }
    }
    int pseudo = 0;
    for (int i = 0; i < 26; ++i) {
        pseudo += min(cs[i], cg[i]);
    }
    return {hits, pseudo};
}

int main() {
    vector<int> ans = masterMind("RGBY", "GGRR");
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
