# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        if node.next is None:
            return node
        
        new_head = self.reverse(node.next)
        node.next.next = node
        node.next = None

        return new_head

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        curr = head
        rev = self.reverse(slow)

        while rev and rev.next:
            currNext = curr.next
            curr.next = rev
            revNext = rev.next
            rev.next = currNext
            rev = revNext
            curr = currNext
        
        return head