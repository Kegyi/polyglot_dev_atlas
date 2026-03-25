#include <iostream>
#include <unordered_set>
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

void removeDuplicateNodes(ListNode* head) {
    std::unordered_set<int> seen;
    ListNode* prev = nullptr;
    ListNode* cur = head;

    while (cur) {
        if (seen.count(cur->val)) {
            prev->next = cur->next;
            cur = cur->next;
            continue;
        }
        seen.insert(cur->val);
        prev = cur;
        cur = cur->next;
    }
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
    ListNode* head = buildList({1, 2, 3, 3, 2, 1, 4});
    removeDuplicateNodes(head);
    printList(head);
    return 0;
}
