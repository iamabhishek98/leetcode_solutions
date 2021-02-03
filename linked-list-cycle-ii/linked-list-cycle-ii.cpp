/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !head->next) return NULL; 
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next;
            if (fast) fast = fast->next;
            if (fast == slow) {
                while(slow!=head)  // to find where the loop  started
            {
                slow=slow->next;
                head=head->next;
            }
            return head;
            }
        }
        return NULL;
    }
};