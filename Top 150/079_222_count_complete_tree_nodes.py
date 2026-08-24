class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0

        left_h = left_height(root.left)
        right_h = left_height(root.right)

        if left_h == right_h:
            return (1 << left_h) + self.countNodes(root.right)
        else:
            return (1 << right_h) + self.countNodes(root.left)