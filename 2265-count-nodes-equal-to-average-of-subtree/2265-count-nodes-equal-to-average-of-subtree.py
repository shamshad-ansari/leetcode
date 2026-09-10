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
            if node is None:
                return 0, 0

            left_sum, left_count = average(node.left)
            right_sum, right_count = average(node.right)

            return (node.val + left_sum + right_sum), (left_count + right_count + 1)

        def solve(node):
            nonlocal count
            if node is None:
                return 
            total_sum, total_count = average(node)
            avg = total_sum//total_count
            if avg == node.val:
                count += 1
                solve(node.left)
                solve(node.right)
            else:
                solve(node.left)
                solve(node.right)
        solve(root)
        return count