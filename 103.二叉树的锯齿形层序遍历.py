#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        queue = [root]

        ans = []

        while queue:
            size = len(queue)
            level = []

            for i in range(size):
                root = queue.pop(0)
                level.append(root.val)

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
            if len(ans) % 2 == 1:
                ans.append(level[::-1])
            else:
                ans.append(level)
            
        return ans

# @lc code=end

