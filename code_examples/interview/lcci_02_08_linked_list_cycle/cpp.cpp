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

bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    ListNode* a = buildList({1, 2, 3, 4});
    ListNode* tail = a;
    while (tail->next) tail = tail->next;
    tail->next = a->next; // create cycle

    ListNode* b = buildList({1, 2, 3, 4});

    std::cout << std::boolalpha << hasCycle(a) << '\n';
    std::cout << std::boolalpha << hasCycle(b) << '\n';
    return 0;
}
