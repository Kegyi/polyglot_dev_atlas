#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

ListNode* partition(ListNode* head, int x) {
    ListNode lessDummy(0), greaterDummy(0);
    ListNode* lessTail = &lessDummy;
    ListNode* greaterTail = &greaterDummy;

    while (head) {
        if (head->val < x) {
            lessTail->next = head;
            lessTail = lessTail->next;
        } else {
            greaterTail->next = head;
            greaterTail = greaterTail->next;
        }
        head = head->next;
    }

    greaterTail->next = nullptr;
    lessTail->next = greaterDummy.next;
    return lessDummy.next;
}

void printList(ListNode* head) {
    bool first = true;
    while (head) {
        if (!first) std::cout << ' ';
        std::cout << head->val;
        first = false;
        head = head->next;
    }
    std::cout << '\n';
}

int main() {
    ListNode* head = buildList({3, 5, 8, 5, 10, 2, 1});
    head = partition(head, 5);
    printList(head);
    return 0;
}
