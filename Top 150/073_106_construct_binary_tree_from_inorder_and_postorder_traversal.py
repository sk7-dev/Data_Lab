import sys
from typing import List, Optional
class Solution:
    def buildTree(
        self,
        inorder: List[int],
        postorder: List[int]
    ) -> Optional[TreeNode]:
        sys.setrecursionlimit(10000)
        inorder_index = {
            value: index for index, value in enumerate(inorder)
        }
        postorder_index = len(postorder) - 1
        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_index
            if left > right:
                return None
            root_value = postorder[postorder_index]
            postorder_index -= 1
            root = TreeNode(root_value)
            middle = inorder_index[root_value]
            root.right = build(middle + 1, right)
            root.left = build(left, middle - 1)
            return root
        return build(0, len(inorder) - 1)