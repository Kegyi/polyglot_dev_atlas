#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

std::vector<int> topKFrequent(const std::vector<int>& nums, int k) {
    std::unordered_map<int, int> freq;
    for (int n : nums) {
        ++freq[n];
    }

    using Entry = std::pair<int, int>;  // (frequency, value)
    auto cmp = [](const Entry& a, const Entry& b) { return a.first > b.first; };
    std::priority_queue<Entry, std::vector<Entry>, decltype(cmp)> minHeap(cmp);

    for (const auto& [value, count] : freq) {
        minHeap.push({count, value});
        if (static_cast<int>(minHeap.size()) > k) {
            minHeap.pop();
        }
    }

    std::vector<int> result;
    while (!minHeap.empty()) {
        result.push_back(minHeap.top().second);
        minHeap.pop();
    }
    std::reverse(result.begin(), result.end());
    return result;
}

int main() {
    const std::vector<int> nums = {1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5};
    const int k = 2;

    const auto result = topKFrequent(nums, k);
    std::cout << "top k frequent:";
    for (int n : result) {
        std::cout << ' ' << n;
    }
    std::cout << '\n';
    return 0;
}
