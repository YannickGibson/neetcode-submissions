# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Trivial solution
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Determine result head
        if list1.val <= list2.val:
            res = list1
            list1 = list1.next
        else:
            res = list2
            list2 = list2.next
        
        tail = res
        while list1 or list2:
            # One is None
            if list2 is None:
                tail.next = list1
                list1 = list1.next
            elif list1 is None:
                tail.next = list2
                list2 = list2.next

            # None are None
            elif list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
        
            # Update tail    
            tail = tail.next
        return res
