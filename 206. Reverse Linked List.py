# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        p, q = head, head.next
        p.next = None

        while q:
            temp = q.next
            q.next = p
            p, q = q, temp

        return p