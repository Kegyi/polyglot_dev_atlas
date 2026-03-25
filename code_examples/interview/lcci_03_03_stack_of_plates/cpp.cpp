#include <iostream>
#include <vector>

class StackOfPlates {
public:
    explicit StackOfPlates(int cap) : capacity(cap) {}

    void push(int val) {
        if (capacity <= 0) return;
        if (stacks.empty() || stacks.back().size() == static_cast<size_t>(capacity)) {
            stacks.push_back({});
        }
        stacks.back().push_back(val);
    }

    int pop() {
        return popAt(static_cast<int>(stacks.size()) - 1);
    }

    int popAt(int index) {
        if (index < 0 || index >= static_cast<int>(stacks.size()) || stacks[index].empty()) {
            return -1;
        }
        int val = stacks[index].back();
        stacks[index].pop_back();
        if (stacks[index].empty()) {
            stacks.erase(stacks.begin() + index);
        }
        return val;
    }

private:
    int capacity;
    std::vector<std::vector<int>> stacks;
};

int main() {
    StackOfPlates s(2);
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    std::cout << s.popAt(0) << '\n';
    std::cout << s.pop() << '\n';
    std::cout << s.pop() << '\n';
    std::cout << s.pop() << '\n';
    return 0;
}
