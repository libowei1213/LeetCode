#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':


        if not root:
            return None

        queue = [root]

        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            for i in range(len(level)):
                if i!=len(level)-1:
                    level[i].next = level[i+1]
                else:
                    level[i].next = None

        return root


        
# @lc code=end

