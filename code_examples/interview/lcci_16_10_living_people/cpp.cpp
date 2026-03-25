#include <iostream>
#include <vector>
using namespace std;

int maxAliveYear(const vector<int>& birth, const vector<int>& death) {
    vector<int> diff(102, 0);
    for (int i = 0; i < static_cast<int>(birth.size()); ++i) {
        ++diff[birth[i] - 1900];
        if (death[i] + 1 <= 2000) {
            --diff[death[i] + 1 - 1900];
        }
    }
    int bestYear = 1900;
    int alive = 0;
    int bestAlive = -1;
    for (int i = 0; i <= 100; ++i) {
        alive += diff[i];
        if (alive > bestAlive) {
            bestAlive = alive;
            bestYear = 1900 + i;
        }
    }
    return bestYear;
}

int main() {
    cout << maxAliveYear({1900, 1901, 1950}, {1948, 1951, 2000}) << endl;
    return 0;
}
