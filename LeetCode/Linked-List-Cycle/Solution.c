#include <stdbool.h>

bool hasCycle(struct ListNode *head) {
    if (!head || !head->next) return false;
    struct ListNode *slow = head;
    struct ListNode *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}
