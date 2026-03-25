#include <iostream>
#include <stack>

class MinStack {
public:
    void push(int x) {
        values.push(x);
        if (mins.empty() || x <= mins.top()) {
            mins.push(x);
        }
    }

    void pop() {
        if (values.empty()) return;
        if (values.top() == mins.top()) {
            mins.pop();
        }
        values.pop();
    }

    int top() const {
        return values.empty() ? -1 : values.top();
    }

    int getMin() const {
        return mins.empty() ? -1 : mins.top();
    }

private:
    std::stack<int> values;
    std::stack<int> mins;
};

int main() {
    MinStack st;
    st.push(3);
    st.push(5);
    st.push(2);
    st.push(2);
    std::cout << st.getMin() << '\n';
    st.pop();
    std::cout << st.getMin() << '\n';
    st.pop();
    std::cout << st.getMin() << '\n';
    return 0;
}
