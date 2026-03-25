#include <iostream>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4, 5};

    for (size_t i = 0; i < values.size(); ++i) {
        std::cout << "for index: " << i << " -> " << values[i] << "\n";
    }

    for (int v : values) {
        if (v == 3) {
            continue;
        }
        std::cout << "range for: " << v << "\n";
    }

    int i = 0;
    while (i < static_cast<int>(values.size())) {
        if (values[i] == 4) {
            break;
        }
        std::cout << "while: " << values[i] << "\n";
        ++i;
    }

    int c = 0;
    do {
        std::cout << "do-while iteration: " << c << "\n";
        ++c;
    } while (c < 2);

    return 0;
}
