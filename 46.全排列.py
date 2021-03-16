#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (77.66%)
# Likes:    1194
# Dislikes: 0
# Total Accepted:    270.5K
# Total Submissions: 348.1K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start

def dfs(result, length, ans, nums):
    if len(result) == length:
        ans.append(result)
        return

    for i in range(len(nums)):
        dfs(result + [nums[i]], length, ans, nums[:i] + nums[i + 1:])

class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        n = len(nums)

        dfs([],n, ans, nums)
        
        return ans



# @lc code=end

