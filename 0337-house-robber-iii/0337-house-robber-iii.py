class Solution:
    def rob(self, root: TreeNode | None) -> int:
        @cache
        def solve(node, taken):
            if not node:
                return 0

            if taken:
                return (
                    node.val
                    + solve(node.left, False)
                    + solve(node.right, False)
                )

            return (
                max(solve(node.left, True), solve(node.left, False))
                + max(solve(node.right, True), solve(node.right, False))
            )

        return max(solve(root, True), solve(root, False))