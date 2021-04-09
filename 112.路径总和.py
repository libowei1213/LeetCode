#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:


        def traverse(ans, root):
            if not root.left and not root.right:
                if ans+root.val == targetSum:
                    return True
                else:
                    return False
            
            if root.left:
                flag = traverse(ans + root.val, root.left)
                if flag:
                    return True
            if root.right:
                flag = traverse(ans + root.val, root.right)
                if flag:
                    return True

            return False
        
        if not root:
            return False

        return traverse(0,root)


# @lc code=end

