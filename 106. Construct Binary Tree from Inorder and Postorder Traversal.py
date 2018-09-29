# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if not postorder:
            return None

        if len(postorder) == 1:
            return TreeNode(postorder[-1])

        root_value = postorder[-1]
        index = inorder.index(root_value)

        root = TreeNode(root_value)

        inorder_left = inorder[:index]
        inorder_right = inorder[index + 1:]

        if inorder_left:
            postorder_left = postorder[:len(inorder_left)]
            root.left = self.buildTree(inorder_left, postorder_left)

        if inorder_right:
            postorder_right = postorder[len(inorder_left):-1]
            root.right = self.buildTree(inorder_right, postorder_right)

        return root
