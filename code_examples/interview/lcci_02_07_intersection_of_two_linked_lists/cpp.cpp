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

ListNode* getIntersectionNode(ListNode* a, ListNode* b) {
    if (!a || !b) return nullptr;
    ListNode* p1 = a;
    ListNode* p2 = b;
    while (p1 != p2) {
        p1 = p1 ? p1->next : b;
        p2 = p2 ? p2->next : a;
    }
    return p1;
}

int main() {
    ListNode* common = buildList({8, 10});

    ListNode* a = buildList({3, 1, 5, 9});
    ListNode* b = buildList({4, 6});

    ListNode* tailA = a;
    while (tailA->next) tailA = tailA->next;
    tailA->next = common;

    ListNode* tailB = b;
    while (tailB->next) tailB = tailB->next;
    tailB->next = common;

    ListNode* intersection = getIntersectionNode(a, b);
    if (intersection) {
        std::cout << intersection->val << '\n';
    } else {
        std::cout << "null\n";
    }
    return 0;
}
