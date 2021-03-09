#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (31.15%)
# Likes:    3062
# Dislikes: 0
# Total Accepted:    440.6K
# Total Submissions: 1.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^5 
# 
# 
#

# @lc code=start
class Solution(object):


    def TwoSum(self, nums, target):
        hash_table = {}
        ans = []
        for i,num in enumerate(nums):
            if target - num not in hash_table:
                hash_table[num] = i
            else:
                ans.append([num,target-num])
        return ans


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            rs = self.TwoSum(nums[i + 1:], -num)
            for r in rs:
                ans.append(",".join(map(lambda x:str(x),sorted([num] + r))))


        ans = set(ans)


        return [[ int(y) for y in x.split(",")] for x in ans]




# @lc code=end

