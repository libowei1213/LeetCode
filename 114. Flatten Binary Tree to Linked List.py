# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        stack = [root]

        last = None

        while stack:
            node = stack.pop()
            if node:

                stack.append(node.right)
                stack.append(node.left)

                if last == None:
                    last = node
                else:
                    last.right = node
                    last.left = None
                    last = node


