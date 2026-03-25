#include <iostream>
#include <string>

enum class Status {
    Pending,
    Running,
    Done,
};

constexpr int kMaxRetries = 3;

std::string to_string(Status status) {
    switch (status) {
        case Status::Pending:
            return "pending";
        case Status::Running:
            return "running";
        case Status::Done:
            return "done";
    }
    return "unknown";
}

int main() {
    Status status = Status::Running;
    std::cout << "status: " << to_string(status) << "\n";
    std::cout << "max retries: " << kMaxRetries << "\n";
    return 0;
}
