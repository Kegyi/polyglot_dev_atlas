#include <chrono>
#include <iostream>

int main() {
    using namespace std::chrono;

    const auto now = system_clock::now();
    const auto later = now + minutes(90);
    const auto now_seconds = duration_cast<seconds>(now.time_since_epoch()).count();
    const auto later_seconds = duration_cast<seconds>(later.time_since_epoch()).count();

    std::cout << "now (epoch seconds): " << now_seconds << "\n";
    std::cout << "later (epoch seconds): " << later_seconds << "\n";
    std::cout << "later > now: " << (later > now) << "\n";
    return 0;
}
