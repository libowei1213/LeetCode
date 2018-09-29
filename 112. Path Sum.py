# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(node, sum, target):
    if not node.left and not node.right:
        if sum + node.val == target:
            return True

    flag = False
    if node.left:
        flag = (flag or dfs(node.left, sum + node.val, target))
    if node.right:
        flag = (flag or dfs(node.right, sum + node.val, target))

    return flag


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        return dfs(root, 0, sum)
