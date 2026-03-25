#include <iostream>
#include <vector>

class TripleInOne {
public:
    TripleInOne(int stackSize)
        : size(stackSize), data(3 * stackSize, 0), tops(3, 0) {}

    void push(int stackNum, int value) {
        if (isFull(stackNum)) return;
        int index = stackNum * size + tops[stackNum];
        data[index] = value;
        tops[stackNum]++;
    }

    int pop(int stackNum) {
        if (isEmpty(stackNum)) return -1;
        tops[stackNum]--;
        int index = stackNum * size + tops[stackNum];
        return data[index];
    }

    int peek(int stackNum) const {
        if (isEmpty(stackNum)) return -1;
        int index = stackNum * size + tops[stackNum] - 1;
        return data[index];
    }

    bool isEmpty(int stackNum) const {
        return tops[stackNum] == 0;
    }

private:
    int size;
    std::vector<int> data;
    std::vector<int> tops;

    bool isFull(int stackNum) const {
        return tops[stackNum] == size;
    }
};

int main() {
    TripleInOne stacks(2);
    stacks.push(0, 10);
    stacks.push(0, 11);
    stacks.push(0, 12);
    stacks.push(1, 20);
    std::cout << stacks.peek(0) << '\n';
    std::cout << stacks.pop(0) << '\n';
    std::cout << stacks.pop(0) << '\n';
    std::cout << stacks.pop(0) << '\n';
    std::cout << std::boolalpha << stacks.isEmpty(1) << '\n';
    return 0;
}
