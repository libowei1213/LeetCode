# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        node_dict = dict()

        p = head

        while p:
            node_dict[p] = RandomListNode(p.label)
            p = p.next

        p = head
        while p:
            node_dict[p].next = node_dict.get(p.next)
            node_dict[p].random = node_dict.get(p.random)
            p = p.next

        return node_dict.get(head)
