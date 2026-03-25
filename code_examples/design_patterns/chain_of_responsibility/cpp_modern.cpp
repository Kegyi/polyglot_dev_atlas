// Modern C++ Chain of Responsibility using std::function
// The chain is a flat vector of handlers; no linked-list of subclasses required.
#include <iostream>
#include <functional>
#include <string>
#include <vector>

struct Request {
    int level;
    std::string message;
};

// Each handler returns true if it handled the request, stopping propagation.
using Handler = std::function<bool(const Request&)>;

void process(const std::vector<Handler>& chain, const Request& req) {
    for (const auto& handler : chain) {
        if (handler(req)) return;
    }
}

int main() {
    std::vector<Handler> chain = {
        [](const Request& req) -> bool {
            if (req.level > 1) return false;
            std::cout << "LowLevelHandler: " << req.message << '\n';
            return true;
        },
        [](const Request& req) -> bool {
            if (req.level != 2) return false;
            std::cout << "MidLevelHandler: " << req.message << '\n';
            return true;
        },
        [](const Request& req) -> bool {
            std::cout << "HighLevelHandler: " << req.message << '\n';
            return true;
        },
    };

    process(chain, {1, "low request"});
    process(chain, {2, "mid request"});
    process(chain, {3, "high request"});
}
