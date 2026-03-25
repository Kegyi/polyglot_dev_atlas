#include <iostream>
#include <stack>

class MyQueue {
public:
    void push(int x) {
        in.push(x);
    }

    int pop() {
        moveIfNeeded();
        if (out.empty()) return -1;
        int v = out.top();
        out.pop();
        return v;
    }

    int peek() {
        moveIfNeeded();
        return out.empty() ? -1 : out.top();
    }

    bool empty() const {
        return in.empty() && out.empty();
    }

private:
    std::stack<int> in;
    std::stack<int> out;

    void moveIfNeeded() {
        if (!out.empty()) return;
        while (!in.empty()) {
            out.push(in.top());
            in.pop();
        }
    }
};

int main() {
    MyQueue q;
    q.push(1);
    q.push(2);
    q.push(3);
    std::cout << q.peek() << '\n';
    std::cout << q.pop() << '\n';
    std::cout << q.pop() << '\n';
    std::cout << std::boolalpha << q.empty() << '\n';
    return 0;
}
