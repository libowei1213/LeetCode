# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def depth(node):
    if not node.left and not node.right:
        return 1

    if node.left and node.right:
        return max(depth(node.left), depth(node.right)) + 1
    if node.left:
        return 1 + depth(node.left)
    else:
        return 1 + depth(node.right)


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return depth(root)
