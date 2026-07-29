class Solution:
    def partition(
        self, head: Optional[ListNode], x: int
    ) -> Optional[ListNode]:
        less_dummy = ListNode()
        greater_dummy = ListNode()
        less_tail = less_dummy
        greater_tail = greater_dummy
        current = head
        while current:
            next_node = current.next
            if current.val < x:
                less_tail.next = current
                less_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
            current = next_node
        greater_tail.next = None
        less_tail.next = greater_dummy.next
        return less_dummy.next