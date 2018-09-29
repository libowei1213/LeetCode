# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if not root:
            return []

        stack = [(root, False)]
        ans = []
        while stack:
            node, visited = stack.pop()

            if visited:
                ans.append(node.val)
            else:
                stack.append((node, True))
                if node.children:
                    for child in node.children[::-1]:
                        stack.append((child, False))
        return ans
