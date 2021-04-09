#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        MAX = float("inf")
        MIN = float("-inf")

        def valid(node, min_val, max_val):
            if not node:
                return True
            if node.val<=min_val or node.val>=max_val:
                return False
            
            
            if not valid(node.right, node.val, max_val):
                return False
            if not valid(node.left, min_val, node.val):
                return False
            return True

        return valid(root, MIN, MAX)


# @lc code=end

