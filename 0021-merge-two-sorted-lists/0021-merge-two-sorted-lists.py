# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tmp = dummy
        h1 = list1
        h2 = list2
        while h1 and h2:
            if h1.val <= h2.val:
                to_append = ListNode(h1.val)
                tmp.next = to_append
                tmp = tmp.next
                h1 = h1.next
            elif h2.val < h1.val:
                to_append = ListNode(h2.val)
                tmp.next = to_append
                tmp = tmp.next
                h2 = h2.next
        if h1:
            tmp.next = h1
        elif h2:
            tmp.next = h2

        return dummy.next


        # Append whats smaller
        # Increment the pointer of the one that you append
        # Loop runs till the smaller of either list exists
        # If any list remains we add it back to our answer