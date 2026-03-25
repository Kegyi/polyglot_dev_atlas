// Modern C++ Command using std::function
// Replaces the command class hierarchy with a simple callable; lambdas capture context directly.
#include <iostream>
#include <functional>
#include <vector>

class Device {
public:
    void turnOn()  const { std::cout << "Device is ON\n"; }
    void turnOff() const { std::cout << "Device is OFF\n"; }
};

int main() {
    Device device;

    // Commands are just callables – no base class, no heap allocation per command
    std::vector<std::function<void()>> commands;
    commands.emplace_back([&device] { device.turnOn();  });
    commands.emplace_back([&device] { device.turnOff(); });

    for (const auto& cmd : commands) {
        cmd();
    }
}
