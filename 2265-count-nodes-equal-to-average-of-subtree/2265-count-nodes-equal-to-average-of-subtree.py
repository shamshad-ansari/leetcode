# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def average(node):
            nonlocal count
            if node is None:
                return 0, 0

            left_sum, left_count = average(node.left)
            right_sum, right_count = average(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = left_count + right_count + 1

            if total_sum// total_count == node.val:
                count += 1

            return total_sum, total_count
        average(root)
        return count