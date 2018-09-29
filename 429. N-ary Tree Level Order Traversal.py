# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = [root]
        ans = []

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.children:
                    for child in node.children:
                        queue.append(child)
            if level:
                ans.append(level)

        return ans
