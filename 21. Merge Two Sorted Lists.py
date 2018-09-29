# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        node1 = l1
        node2 = l2

        newList = ListNode(0)
        node = newList

        while node1 or node2:
            if not node1:
                value = node2.val
                node2 = node2.next
            elif not node2:
                value = node1.val
                node1 = node1.next

            elif node1 and node2:
                if node1.val < node2.val:
                    value = node1.val
                    node1 = node1.next
                else:
                    value = node2.val
                    node2 = node2.next
            node.next = ListNode(value)
            node = node.next

        return newList.next