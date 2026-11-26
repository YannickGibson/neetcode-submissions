# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, root: Optional[ListNode]) -> None:
        # 0, 1, 2, 3, 4, 5, 6
        # 0, 6, 1, 5, 2, 4, 3
        # last is 7 // 2 == 3
        # 0, 1, 2, 3, 4, 5
        # 0, 5, 1, 4, 2, 3
        # last 6 // 2 == 3 

        l = []

        def dfs(node, index=0):

            if not node: return
            # 0, 1, 2, 3
            # 0, 3, 1, 2

            l.append(node)
            dfs(node.next, index+1)

            if index < len(l) // 2:
                node.next = l[len(l) - index - 1]
            elif index == len(l) // 2:
                node.next = None
            else:
                node.next = l[len(l) - index]

        dfs(root)
        return None
