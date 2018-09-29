# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        flag = 0

        node1 = l1
        node2 = l2

        newList = ListNode(0)

        p = newList

        while (node1 or node2):

            if node1:
                value = node1.val
                node1 = node1.next
            else:
                value = 0
                node1 = None

            if node2:
                value2 = node2.val
                node2 = node2.next
            else:
                value2 = 0
                node2 = None

            p.next = ListNode(flag + value + value2)

            if p.next.val >= 10:
                p.next.val -= 10
                flag = 1
            else:
                flag = 0

            p = p.next

        if flag == 1:
            p.next = ListNode(1)

        return newList.next
