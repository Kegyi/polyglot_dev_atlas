#include <iostream>
#include <queue>
#include <vector>

int main() {
    // max-heap (default)
    std::priority_queue<int> maxHeap;
    for (int v : {3, 1, 4, 1, 5, 9}) maxHeap.push(v);
    std::cout << "max: " << maxHeap.top() << "\n";  // 9

    // min-heap via greater<>
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    for (int v : {3, 1, 4, 1, 5, 9}) minHeap.push(v);
    std::cout << "drain min-heap: ";
    while (!minHeap.empty()) {
        std::cout << minHeap.top() << ' ';
        minHeap.pop();
    }
    std::cout << "\n";  // 1 1 3 4 5 9
    return 0;
}
