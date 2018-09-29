# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        root = TreeNode(pre.pop(0))
        post.pop(-1)

        if pre:
            index = post.index(pre[0])
            split = max([pre.index(post[i]) for i in range(index + 1)])
            left_pre = pre[:split + 1]
            right_pre = pre[split + 1:]
            left_post = post[:index + 1]
            right_post = post[index + 1:]

            if left_pre:
                root.left = self.constructFromPrePost(left_pre, left_post)

            if right_pre:
                root.right = self.constructFromPrePost(right_pre, right_post)

        return root


if __name__ == '__main__':
    r = Solution().constructFromPrePost([1, 2, 3, 4], [3, 4, 2, 1])
