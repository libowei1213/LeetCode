# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_value = preorder[0]
        index = inorder.index(root_value)

        root = TreeNode(root_value)

        inorder_left = inorder[:index]
        inorder_right = inorder[index + 1:]

        if inorder_left:
            preorder_left = preorder[1:1 + len(inorder_left)]
            root.left = self.buildTree(preorder_left, inorder_left)

        if inorder_right:
            preorder_right = preorder[1 + len(inorder_left):]
            root.right = self.buildTree(preorder_right, inorder_right)

        return root
