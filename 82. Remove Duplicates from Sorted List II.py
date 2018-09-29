# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dump = ListNode(0)
        dump.next = head

        pre, p, q = dump, head, head.next

        isDulp = False

        while q:
            if p.val == q.val:
                q = q.next
                isDulp = True
            else:
                if isDulp:
                    pre.next = q
                    p, q = q, q.next
                else:
                    pre, p, q = p, q, q.next
                isDulp = False

        if isDulp:
            pre.next = q

        return dump.next
