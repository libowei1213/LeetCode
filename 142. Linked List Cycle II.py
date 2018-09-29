# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                break

            slow = slow.next
            fast = fast.next.next
        else:
            return None

        while head != slow.next:
            head = head.next
            slow = slow.next

        return head
