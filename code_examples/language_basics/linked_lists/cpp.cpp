#include <iostream>

struct Node {
    int value;
    Node* next;
    explicit Node(int v) : value(v), next(nullptr) {}
};

void printList(Node* head) {
    for (Node* cur = head; cur; cur = cur->next) {
        std::cout << cur->value;
        if (cur->next) std::cout << " -> ";
    }
    std::cout << "\n";
}

Node* prepend(Node* head, int value) {
    Node* node = new Node(value);
    node->next = head;
    return node;
}

Node* removeValue(Node* head, int value) {
    if (!head) return nullptr;
    if (head->value == value) {
        Node* next = head->next;
        delete head;
        return next;
    }
    head->next = removeValue(head->next, value);
    return head;
}

int main() {
    Node* head = nullptr;
    for (int v : {3, 2, 1}) head = prepend(head, v);  // 1 -> 2 -> 3
    printList(head);
    head = removeValue(head, 2);
    printList(head);  // 1 -> 3
    while (head) { Node* next = head->next; delete head; head = next; }
    return 0;
}
