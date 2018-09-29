# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        length = 0

        node = head
        while node:
            node = node.next
            length += 1

        # 删除第一个节点
        if length == n:
            head = head.next
            return head

        node = head
        for i in range(length - n - 1):
            node = node.next

        node.next = node.next.next

        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)

    s = Solution()
    r = s.removeNthFromEnd(head, 2)

    while r:
        print(r.val)
        r = r.next
