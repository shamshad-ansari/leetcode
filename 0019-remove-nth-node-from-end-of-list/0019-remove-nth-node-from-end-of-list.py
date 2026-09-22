# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next    
        
        if count == 1 and n == 1:
            return None
        
        toReach = count - n

        if toReach == 0:
            return head.next

        tmp = head
        count = 0
        while tmp:
            count += 1
            if count == toReach:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
        return head