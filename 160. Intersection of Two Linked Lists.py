# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None

        p = headA
        q = headB

        while p != q:
            if p:
                p = p.next
            else:
                p = headB

            if q:
                q = q.next
            else:
                q = headA

        return p
