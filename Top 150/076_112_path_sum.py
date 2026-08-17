class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False 
        if root.left is None and root.right is None:
            return targetSum == root.val
        remaining = targetSum - root.val
        return (
            self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining)
        )