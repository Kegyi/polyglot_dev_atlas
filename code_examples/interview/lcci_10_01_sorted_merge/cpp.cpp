#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& a, int m, const vector<int>& b, int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;
    while (j >= 0) {
        if (i >= 0 && a[i] > b[j]) {
            a[k--] = a[i--];
        } else {
            a[k--] = b[j--];
        }
    }
}

int main() {
    vector<int> a = {1, 2, 3, 0, 0, 0};
    vector<int> b = {2, 5, 6};
    merge(a, 3, b, 3);
    cout << "[";
    for (int i = 0; i < static_cast<int>(a.size()); ++i) {
        if (i) cout << ", ";
        cout << a[i];
    }
    cout << "]" << endl;
    return 0;
}
