#include <iostream>
#include <stack>
#include <vector>

void sortStack(std::stack<int>& st) {
    std::stack<int> tmp;

    while (!st.empty()) {
        int cur = st.top();
        st.pop();
        while (!tmp.empty() && tmp.top() > cur) {
            st.push(tmp.top());
            tmp.pop();
        }
        tmp.push(cur);
    }

    while (!tmp.empty()) {
        st.push(tmp.top());
        tmp.pop();
    }
}

void printStackTopToBottom(std::stack<int> st) {
    bool first = true;
    while (!st.empty()) {
        if (!first) std::cout << ' ';
        std::cout << st.top();
        st.pop();
        first = false;
    }
    std::cout << '\n';
}

int main() {
    std::stack<int> st;
    for (int n : std::vector<int>{3, 1, 4, 2}) {
        st.push(n);
    }
    sortStack(st);
    printStackTopToBottom(st);
    return 0;
}
