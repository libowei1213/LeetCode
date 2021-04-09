#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def build(inorder, postorder):
            if not inorder:
                return None
            if len(inorder) == 1:
                return TreeNode(inorder[0])
            
            val = postorder.pop()
            node = TreeNode(val)

            index = inorder.index(val)
            node.left = build(inorder[:index], postorder[:index])
            node.right = build(inorder[index + 1:], postorder[index:])
            return node

        return build(inorder,postorder)

            

# @lc code=end

