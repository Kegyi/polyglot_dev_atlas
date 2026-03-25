#include <iostream>
#include <vector>
#include <functional>
using namespace std;

void hanota(vector<int>& A, vector<int>& B, vector<int>& C) {
    function<void(int, vector<int>&, vector<int>&, vector<int>&)> move =
        [&](int n, vector<int>& src, vector<int>& aux, vector<int>& dst) {
            if (n == 0) return;
            move(n - 1, src, dst, aux);
            dst.push_back(src.back());
            src.pop_back();
            move(n - 1, aux, src, dst);
        };
    move((int)A.size(), A, B, C);
}

int main() {
    vector<int> A = {2, 1, 0}, B = {}, C = {};
    hanota(A, B, C);
    cout << "A: ["; for (int i = 0; i < (int)A.size(); i++) cout << (i?",":"") << A[i]; cout << "]" << endl;
    cout << "B: ["; for (int i = 0; i < (int)B.size(); i++) cout << (i?",":"") << B[i]; cout << "]" << endl;
    cout << "C: ["; for (int i = 0; i < (int)C.size(); i++) cout << (i?",":"") << C[i]; cout << "]" << endl;
    return 0;
}
