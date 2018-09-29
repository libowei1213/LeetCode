# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        stack = []

        answer = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            if stack:
                root = stack.pop(-1)
                answer.append(root.val)
                root = root.right

        return answer
