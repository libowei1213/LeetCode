# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

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

        for i in range(len(answer) - 1):
            if answer[i] >= answer[i + 1]:
                return False

        return True
