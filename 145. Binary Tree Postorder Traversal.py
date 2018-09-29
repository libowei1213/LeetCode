# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        stack = [[root, False]]

        ans = []

        while stack:
            node, visited = stack.pop()
            if visited:
                ans.append(node.val)
            else:
                stack.append([node, True])
                if node.right:
                    stack.append([node.right, False])
                if node.left:
                    stack.append([node.left, False])

        return ans
