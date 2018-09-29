# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        size = len(lists)

        if size == 0:
            return []

        if size == 1:
            return lists[0]


        index = [i for i in range()]

        while len(lists) > 1:
            for i in range(0, len(lists) - 1, 2)[::-1]:
                l1 = lists[i]
                l2 = lists[i + 1]

                lists[i] = self.merge2Lists(l1, l2)
                lists.remove(l2)
        return lists[0]

    def merge2Lists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        node1 = l1
        node2 = l2

        head = ListNode(0)
        l = head

        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                l.next = ListNode(node1.val)
                node1 = node1.next
            else:
                l.next = ListNode(node2.val)
                node2 = node2.next

            l = l.next

        while node1 != None:
            l.next = ListNode(node1.val)
            node1 = node1.next
            l = l.next

        while node2 != None:
            l.next = ListNode(node2.val)
            node2 = node2.next
            l = l.next

        return head.next


if __name__ == '__main__':
    l1 = None

    l2 = ListNode(-1)
    l2.next = ListNode(5)
    l2.next.next = ListNode(11)

    l3 = None

    l4 = ListNode(6)
    l4.next = ListNode(10)

    s = Solution()
    r = s.mergeKLists([l1, l2, l3, l4])

    while r:
        print(r.val)
        r = r.next
