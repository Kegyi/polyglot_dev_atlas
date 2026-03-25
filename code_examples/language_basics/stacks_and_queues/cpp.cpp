#include <iostream>
#include <queue>
#include <stack>

int main() {
    std::stack<int> stk;
    for (int v : {1, 2, 3}) stk.push(v);
    std::cout << "stack top: " << stk.top() << "\n";  // 3 (LIFO)
    stk.pop();
    std::cout << "after pop: " << stk.top() << "\n";  // 2

    std::queue<int> q;
    for (int v : {1, 2, 3}) q.push(v);
    std::cout << "queue front: " << q.front() << "\n";  // 1 (FIFO)
    q.pop();
    std::cout << "after dequeue: " << q.front() << "\n";  // 2
    return 0;
}
