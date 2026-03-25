#include <iostream>
#include <string>
#include <vector>
using namespace std;

int findString(const vector<string>& words, const string& target) {
    int left = 0;
    int right = static_cast<int>(words.size()) - 1;
    int answer = -1;

    while (left <= right) {
        int mid = (left + right) >> 1;
        int l = mid;
        int r = mid;
        int actual = -1;
        while (l >= left || r <= right) {
            if (l >= left && !words[l].empty()) {
                actual = l;
                break;
            }
            if (r <= right && !words[r].empty()) {
                actual = r;
                break;
            }
            --l;
            ++r;
        }
        if (actual == -1) {
            break;
        }
        if (words[actual] == target) {
            answer = actual;
            right = actual - 1;
        } else if (words[actual] < target) {
            left = actual + 1;
        } else {
            right = actual - 1;
        }
    }
    return answer;
}

int main() {
    vector<string> words = {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""};
    cout << findString(words, "ta") << endl;
    cout << findString(words, "ball") << endl;
    return 0;
}
