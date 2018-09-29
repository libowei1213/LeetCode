# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or k == 0:
            return head

        size = 1
        p = head
        while p.next:
            p = p.next
            size += 1
        p.next = head

        step = size - k % size

        p = head
        for _ in range(step - 1):
            p = p.next

        head = p.next
        p.next = None
        return head
