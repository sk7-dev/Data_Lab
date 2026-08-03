class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def are_mirrors(left: Optional[TreeNode],
                        right: Optional[TreeNode]) -> bool:
            if left is None or right is None:
                return left is right
            return (
                left.val == right.val
                and are_mirrors(left.left, right.right)
                and are_mirrors(left.right, right.left)
            )
        return are_mirrors(root.left, root.right)