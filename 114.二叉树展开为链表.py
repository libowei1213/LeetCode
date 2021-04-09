#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        def traverse(root,ans):
            ans.append(root)
            if root.left:
                traverse(root.left,ans)
            if root.right:
                traverse(root.right,ans)

        ans = []
        traverse(root,ans)


        for i in range(len(ans)-1):
            ans[i].left = None
            ans[i].right = ans[i+1]
        


# @lc code=end

