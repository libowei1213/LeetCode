#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def valid(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False

            return valid(a.left, b.right) and valid(a.right, b.left)
            
        
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        if not root.left or not root.right:
            return False

        return valid(root.left,root.right)

# @lc code=end

