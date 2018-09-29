# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def nextNode(self, stack):

        if not stack:
            return None

        root = stack.pop(-1)

        if not root.left and not root.right:
            return root.val
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

        return self.nextNode(stack)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        stack1 = [root1]
        stack2 = [root2]
        while stack1 and stack2:
            t1 = self.nextNode(stack1)
            t2 = self.nextNode(stack2)

            if not t1 and not t2:
                return True

            if not t1 or not t2:
                return False

            if t1 == t2:
                continue
            else:
                return False

        return True
