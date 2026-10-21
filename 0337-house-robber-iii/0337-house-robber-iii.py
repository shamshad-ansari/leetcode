# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        @cache
        def solve(node, parent_taken):
            if not node:
                return 0

            skip = solve(node.left, False) + solve(node.right, False)

            take = 0
            if not parent_taken:
                take += node.val + solve(node.left, True) + solve(node.right, True)

            return max(take,skip)
        
        return solve(root, False)