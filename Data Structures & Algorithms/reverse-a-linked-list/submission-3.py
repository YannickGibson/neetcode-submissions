# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
        
        nxt = head
        head = None

        while nxt:
            tmp = nxt.next
            nxt.next = head
            head = nxt
            nxt = tmp

        return head
