#include <iostream>
#include <vector>
using namespace std;

vector<int> swapNumbers(vector<int> numbers) {
    return {numbers[1], numbers[0]};
}

int main() {
    vector<int> numbers = {1, 2};
    vector<int> ans = swapNumbers(numbers);
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
