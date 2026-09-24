# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        space = []
        temp = head
        while temp:
            space.append(temp)
            temp = temp.next
        
        space = sorted(space, key = lambda x : x.val)

        temp = space[0]
        for i in range(len(space)-1):
            node = space[i]
            node.next = space[i+1]

        space[-1].next = None
        return space[0]