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

bool deleteMiddleNode(ListNode* node) {
    if (!node || !node->next) {
        return false;
    }
    node->val = node->next->val;
    node->next = node->next->next;
    return true;
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
    ListNode* head = buildList({1, 2, 3, 4, 5});
    ListNode* node = head->next->next;
    deleteMiddleNode(node);
    printList(head);
    return 0;
}
