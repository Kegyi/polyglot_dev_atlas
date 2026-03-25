#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4, 5};

    std::cout << "original: ";
    for (int v : values) {
        std::cout << v << ' ';
    }
    std::cout << "\n";

    std::vector<int> doubled(values.size());
    std::transform(values.begin(), values.end(), doubled.begin(), [](int x) {
        return x * 2;
    });

    std::vector<int> evens;
    std::copy_if(doubled.begin(), doubled.end(), std::back_inserter(evens), [](int x) {
        return x % 2 == 0;
    });

    int total = std::accumulate(evens.begin(), evens.end(), 0);
    std::cout << "sum of evens in doubled: " << total << "\n";
    return 0;
}
