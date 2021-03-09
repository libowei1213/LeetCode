#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.55%)
# Likes:    514
# Dislikes: 0
# Total Accepted:    139K
# Total Submissions: 181.6K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start


def dfs(result, ans, k, nums):
    if len(ans) == k:
        result.append(ans)
        return
    for i in range(len(nums)):
        dfs(result, ans+[nums[i]],k, nums[i+1:])



class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


        nums = [i for i in range(1, n + 1)]
        
        result = []


        dfs(result, [], k, nums)
        
        return result




# @lc code=end

