# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find middle
        fast = head.next  # Esentially marks when we can end
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse pointers in second half
        curr = slow.next
        prev = slow.next = None
        # a -> b -> ... -> e -> f -> g ->
        #                  pr <-curr nxt
        #                       pr   curr
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        # Merge lists
        # 2, 4
        # 8, 6
        # tmp = 4
        # tmp2 = 6
        # 2 -> 8 -> 4
        # head = 4
        # head2 = 6
        # ====
        # tmp = None
        # tmp2 = None
        # 2 -> 8 -> 4 -> 6 -> None
        # head = None
        # head2 = None  
        head2 = prev
        while head2:
            tmp, tmp2 = head.next, head2.next
            head.next = head2
            head2.next = tmp
            head = tmp
            head2 = tmp2

