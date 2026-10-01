# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        main = []
        for arr in lists:
            while arr:
                main.append(arr.val)
                arr = arr.next

        
        main.sort()

        res = ListNode(0)
        curr = res
        for n in main:
            curr.next = ListNode(n)
            curr = curr.next
        return res.next


        