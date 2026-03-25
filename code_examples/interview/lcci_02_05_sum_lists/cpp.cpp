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

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    int carry = 0;

    while (l1 || l2 || carry) {
        int sum = carry;
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }

        tail->next = new ListNode(sum % 10);
        tail = tail->next;
        carry = sum / 10;
    }

    return dummy.next;
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
    ListNode* a = buildList({7, 1, 6}); // 617
    ListNode* b = buildList({5, 9, 2}); // 295
    ListNode* c = addTwoNumbers(a, b);  // 912 -> 2 1 9
    printList(c);
    return 0;
}
