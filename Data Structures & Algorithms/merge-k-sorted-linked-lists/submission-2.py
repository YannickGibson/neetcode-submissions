# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        
        
        dummy = ListNode()
        tail = dummy
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        # i is dummy so obj is never compared

        heads = [head for head in lists if head]
        order = len(lists)

        heapq.heapify(heap)  # O(k)

        while heap:

            #min_head = None
            #min_val = 10001
            # for head in heads:
            #     if min_head is None or head.val < min_val:
            #         min_head = head
            #         min_val = head.val
            
            _, _, min_head = heapq.heappop(heap)

            if min_head.next:
                heapq.heappush(heap, (min_head.next.val, order, min_head.next))
                order += 1
                #heads.append(min_head.next)
            #heads.remove(min_head)
            

            tail.next = min_head
            tail = tail.next


        return dummy.next