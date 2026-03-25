#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> values{9, 3, 7, 1, 5};
    std::sort(values.begin(), values.end());

    bool has_seven = std::binary_search(values.begin(), values.end(), 7);
    auto it = std::lower_bound(values.begin(), values.end(), 7);
    int index = (it != values.end() && *it == 7) ? static_cast<int>(it - values.begin()) : -1;

    std::cout << "sorted: ";
    for (int v : values) {
        std::cout << v << ' ';
    }
    std::cout << "\ncontains 7: " << has_seven << "\nindex of 7: " << index << "\n";
    return 0;
}
