# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        length = 0
        p = head

        while p:
            length += 1
            p = p.next

        length = length // 2 + 1

        node = ListNode(0)
        node.next = head

        for i in range(length):
            node = node.next

        return node
