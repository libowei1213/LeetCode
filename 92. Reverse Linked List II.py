# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        start = dummy
        for _ in range(m - 1):
            start = start.next

        end = start.next

        p, q = start.next, start.next.next

        for _ in range(n - m):
            temp = q.next
            q.next = p
            p, q = q, temp

        end.next = q
        start.next = p

        return dummy.next
