# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        tail = None
        carry = 0

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            x = (a + b + carry)
            mod_sum = x % 10

            tmp = ListNode(mod_sum, None)
            if res is None or tail is None:
                res = tmp
            else:
                tail.next = tmp

            # Prepare for next pair
            tail = tmp
            carry = x // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Carry to last new node
        if carry > 0:
            tail.next = ListNode(carry, None)

        return res
        