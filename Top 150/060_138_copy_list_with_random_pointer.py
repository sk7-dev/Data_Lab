class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # 1. Insert each copied node directly after its original node.
        current = head
        while current:
            copied = Node(current.val)
            copied.next = current.next
            current.next = copied
            current = copied.next

        # 2. Assign random pointers for the copied nodes.
        current = head
        while current:
            copied = current.next
            copied.random = (
                current.random.next
                if current.random is not None
                else None
            )
            current = copied.next

        # 3. Separate the original and copied linked lists.
        copied_head = head.next
        current = head

        while current:
            copied = current.next
            current.next = copied.next

            if copied.next is not None:
                copied.next = copied.next.next

            current = current.next

        return copied_head