# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        space = []
        temp = head
        while temp:
            space.append(temp)
            temp = temp.next
        
        i = 0
        j = len(space) - 1

        while i < j:
            space[i].next = space[j]
            i += 1
            if i == j:
                break
            space[j].next = space[i]
            j -= 1   
        
        space[i].next = None
        return space[i]