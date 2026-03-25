#include <iostream>
#include <vector>
#include <numeric>
#include <future>
#include <thread>
#include <algorithm>

int partial_sum(const std::vector<int>& v, size_t start, size_t len) {
    return std::accumulate(v.begin() + start, v.begin() + start + len, 0);
}

int main() {
    const size_t N = 1000;
    std::vector<int> data(N);
    std::iota(data.begin(), data.end(), 1);
    size_t threads = std::thread::hardware_concurrency();
    if (threads == 0) threads = 4;
    size_t block = data.size() / threads;
    std::vector<std::future<int>> futs;
    for (size_t i = 0; i < threads; ++i) {
        size_t s = i * block;
        size_t len = (i + 1 == threads) ? data.size() - s : block;
        futs.push_back(std::async(std::launch::async, [s, len, &data]() {
            return partial_sum(data, s, len);
        }));
    }
    int total = 0;
    for (auto &f : futs) total += f.get();
    std::cout << "Total: " << total << std::endl;
    return 0;
}
