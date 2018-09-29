# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue1 = [root]
        queue2 = []

        answers = []

        while queue1 or queue2:

            level = []
            while queue1:
                node = queue1.pop(0)
                level.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            if level:
                answers.append(level)

            level = []
            while queue2:
                node = queue2.pop(0)
                level.append(node.val)
                if node.left:
                    queue1.append(node.left)
                if node.right:
                    queue1.append(node.right)
            if level:
                answers.append(level)

        return answers[::-1]
