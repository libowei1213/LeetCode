#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (62.85%)
# Likes:    623
# Dislikes: 0
# Total Accepted:    144.2K
# Total Submissions: 229.2K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# 
# 
#

# @lc code=start


def dfs(result, n, ans, nums):
    if len(result) == n:
        ans.append(result)
        return

    for i in range(len(nums)):
        if (result and result[-1] != nums[i]) or result==[]:
            dfs(result+[nums[i]],n,ans, nums[:i]+nums[i+1:])


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        n = len(nums)

        ans = []

        dfs([],n,ans,nums)

        # for i in range(len(nums)):
        #     if i == 0:
        #         dfs([nums[i]], n, ans, nums[i + 1:])
        #     elif i - 1 >= 0 and nums[i] != nums[i - 1]:
        #         dfs([nums[i]], n, ans, nums[:i] + nums[i + 1:])
        
        return ans
                



# @lc code=end

