class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float("-inf")
        def dfs(node):
            nonlocal maximum
            if node is None:
                return 0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            path_sum = node.val + left_gain + right_gain
            maximum = max(maximum, path_sum)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return maximum