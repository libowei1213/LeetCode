# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(node, depth, result):
    if not node.left and not node.right:
        result.append(depth)

    if node.left:
        dfs(node.left, depth + 1, result)
    if node.right:
        dfs(node.right, depth + 1, result)


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        r = []
        dfs(root, 1, r)
        return min(r)
