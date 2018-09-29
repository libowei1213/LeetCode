# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = ListNode(0)
        p0 = p
        p.next = head

        while p.next and p.next.next:
            p1, p2 = p.next, p.next.next
            p.next, p1.next, p2.next = p2, p2.next, p1
            p = p.next.next

        return p0.next


if __name__ == '__main__':
    l2 = ListNode(-1)
    l2.next = ListNode(5)
    l2.next.next = ListNode(11)
    # l2.next.next.next = ListNode(20)

    s = Solution()
    r = s.swapPairs(l2)

    while r:
        print(r.val)
        r = r.next
