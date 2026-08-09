class Node:
    def __init__(
        self,
        val: int = 0,
        left: 'Node' = None,
        right: 'Node' = None,
        next: 'Node' = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        current_level = root
        while current_level:
            dummy = Node(0)
            tail = dummy
            current = current_level
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next
            current_level = dummy.next
        return root