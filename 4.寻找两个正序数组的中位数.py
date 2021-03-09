#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.67%)
# Likes:    3789
# Dislikes: 0
# Total Accepted:    350.2K
# Total Submissions: 881.9K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 
# 
# 示例 3：
# 
# 
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
# 
# 
# 示例 4：
# 
# 
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 
# 
# 示例 5：
# 
# 
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
# 
# 
# 
# 
# 提示：
# 
# 
# nums1.length == m
# nums2.length == n
# 0 
# 0 
# 1 
# -10^6 
# 
# 
# 
# 
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
# 
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        i = 0
        j = 0

        merged_nums = []

        while i < len(nums1) or j < len(nums2):

            if i<len(nums1) and j<len(nums2):
                if nums1[i] <= nums2[j]:
                    merged_nums.append(nums1[i])
                    i += 1
                else:
                    merged_nums.append(nums2[j])
                    j += 1
            else:
                if i < len(nums1):
                    merged_nums.append(nums1[i])
                    i += 1
                if j < len(nums2):
                    merged_nums.append(nums2[j])
                    j += 1


        print(merged_nums)

        length = len(merged_nums)

        if length % 2 == 0:
            return (merged_nums[length // 2] + merged_nums[length // 2 - 1]) / 2.0
        else:
            return  (merged_nums[(length-1)//2])





# @lc code=end

