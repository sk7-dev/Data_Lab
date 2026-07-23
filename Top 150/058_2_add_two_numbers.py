class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 is not None or l2 is not None or carry:
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0
            total = value1 + value2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next