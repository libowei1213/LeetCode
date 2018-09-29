# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(node, path, sum, target, answers):
    if not node.left and not node.right:
        if sum + node.val == target:
            answers.append(path + [node.val])

    if node.left:
        dfs(node.left, path + [node.val], sum + node.val, target, answers)
    if node.right:
        dfs(node.right, path + [node.val], sum + node.val, target, answers)


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        ans = []
        dfs(root, [], 0, sum, ans)
        return ans