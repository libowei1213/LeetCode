#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':


        if not head:
            return None
        
        dummy = Node(0)
        dummy.next = head

        p = head
        while p:
            node = Node(p.val)
            temp = p.next
            p.next = node
            node.next = temp
            p = temp

        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            else:
                p.next.random = None

            p = p.next.next

        p = head.next
        while p.next:
            p.next =p.next.next
            p = p.next

        return head.next

        
            


        
# @lc code=end

