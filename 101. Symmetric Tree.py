# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def judge(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False

    if a.val != b.val:
        return False

    return judge(a.left, b.right) and judge(a.right, b.left)


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        return judge(root.left, root.right)
