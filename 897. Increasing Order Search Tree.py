# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        newTree = TreeNode(0)
        tree = newTree

        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            if stack:
                root = stack.pop(-1)
                print(root.val)
                tree.right = TreeNode(root.val)
                tree = tree.right
                root = root.right

        return newTree.right


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)

    Solution().increasingBST(root)
