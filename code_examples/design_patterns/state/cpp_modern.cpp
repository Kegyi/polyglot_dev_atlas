// Modern C++ State using std::variant
// States are plain value types; transitions are just assignments.
// No virtual dispatch, no heap allocation, exhaustive state handling enforced by the compiler.
#include <iostream>
#include <variant>

struct StartState   { void handle() const { std::cout << "Entering start state\n"; } };
struct RunningState { void handle() const { std::cout << "Running state active\n"; } };
struct StoppedState { void handle() const { std::cout << "Stopped state active\n"; } };

using State = std::variant<StartState, RunningState, StoppedState>;

void handle(const State& state) {
    std::visit([](const auto& s) { s.handle(); }, state);
}

int main() {
    State state = StartState{};
    handle(state);

    state = RunningState{};
    handle(state);

    state = StoppedState{};
    handle(state);
}
