// Modern C++ Observer using std::function callbacks
// Removes the Observer interface; any callable (lambda, free function, member) subscribes directly.
#include <iostream>
#include <functional>
#include <string>
#include <vector>

class Subject {
public:
    using Listener = std::function<void(const std::string&)>;

    void subscribe(Listener listener) {
        listeners_.push_back(std::move(listener));
    }

    void notify(const std::string& msg) const {
        for (const auto& listener : listeners_) {
            listener(msg);
        }
    }

private:
    std::vector<Listener> listeners_;
};

int main() {
    Subject subject;

    // Lambdas subscribe directly – no Observer subclass needed
    subject.subscribe([](const std::string& msg) {
        std::cout << "Observer1 received: " << msg << '\n';
    });
    subject.subscribe([](const std::string& msg) {
        std::cout << "Observer2 received: " << msg << '\n';
    });

    subject.notify("Event 1");
    subject.notify("Event 2");
}
