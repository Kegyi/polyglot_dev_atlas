#include <iostream>
using namespace std;

int maximum(int a, int b) {
    return a > b ? a : b;
}

int main() {
    cout << maximum(1, 2) << endl;
    return 0;
}
