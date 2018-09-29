# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        mid = 0
        slow, fast = ListNode(0), ListNode(0)
        slow.next = head
        fast.next = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            mid += 1

        p, q = slow, slow.next

        while q:
            temp = q.next
            q.next = p
            p, q = q, temp

        left, right = head, p
        for i in range(mid):
            if left.val != right.val:
                return False
            left, right = left.next, right.next

        return True
