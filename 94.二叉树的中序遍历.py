#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def traversal(root, path):
            if not root:
                return

            traversal(root.left, path)
            path.append(root.val)
            traversal(root.right, path)

        result = []

        traversal(root, result)

        return result


# @lc code=end
