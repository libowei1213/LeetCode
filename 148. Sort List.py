# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(p1, p2):
    head = ListNode(0)

    last = head

    while p1 and p2:
        if p1.val <= p2.val:
            last.next = p1
            p1 = p1.next
        else:
            last.next = p2
            p2 = p2.next
        last = last.next

    if p1:
        last.next = p1
    if p2:
        last.next = p2

    return head.next


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        p1 = self.sortList(head)
        p2 = self.sortList(right)
        return merge(p1, p2)


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(4)

    r = Solution().sortList(head)

    while r:
        print(r.val)
        r=r.next
