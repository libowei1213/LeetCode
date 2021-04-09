#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.maxValue = -float("inf")

    def maxPathSum(self, root: TreeNode) -> int:

        def maxGain(root):
            if not root:
                return 0

            leftGain = max([maxGain(root.left),0])
            rightGain = max([maxGain(root.right),0])

            value = leftGain + rightGain + root.val
            self.maxValue = max([self.maxValue,value])

            return root.val + max([leftGain,rightGain])

        maxGain(root)
        return self.maxValue


# @lc code=end

