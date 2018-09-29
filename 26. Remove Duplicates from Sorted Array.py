# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverse(self, pre, k):
        p = pre.next
        first = pre.next

        q = p.next

        for _ in range(k - 1):
            temp = q.next
            q.next = p
            p, q = q, temp

        pre.next = p
        first.next = q

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k == 1:
            return head

        count = 0
        p = head
        while p:
            count += 1
            p = p.next

        reverseCount = count // k

        dummpy = ListNode(0)
        dummpy.next = head

        p = dummpy

        index = 0
        while p:
            if index % k == 0 and reverseCount > 0:
                self.reverse(p, k)
                reverseCount -= 1
            p = p.next
            index += 1

        return dummpy.next
