# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        prev = head
        tmp = head.next
        count = 2
        while tmp and tmp.next:
            nxt = tmp.next
            if tmp.val > prev.val and tmp.val > nxt.val:
                arr.append(count)
            elif tmp.val < prev.val and tmp.val < nxt.val:
                arr.append(count)
            prev = tmp
            tmp = nxt
            count += 1

        if len(arr) < 2:
            return [-1, -1]

        min_dist = float("inf")

        for i in range(1, len(arr)):
            min_dist = min(min_dist, arr[i] - arr[i - 1])

        max_dist = arr[-1] - arr[0]

        return [min_dist, max_dist]