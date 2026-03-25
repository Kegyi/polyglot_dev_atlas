#include <iostream>
using namespace std;

class Operations {
public:
    int minus(int a, int b) {
        return a - b;
    }

    int multiply(int a, int b) {
        return a * b;
    }

    int divide(int a, int b) {
        return a / b;
    }
};

int main() {
    Operations ops;
    cout << ops.minus(10, 3) << endl;
    cout << ops.multiply(6, -4) << endl;
    cout << ops.divide(20, 5) << endl;
    return 0;
}
