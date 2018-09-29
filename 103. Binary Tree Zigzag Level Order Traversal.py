# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = [root]

        answers = []

        level = 0
        while queue:
            level += 1
            temp = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                if level & 1 == 1:
                    answers.append(temp)
                else:
                    answers.append(temp[::-1])

        return answers
