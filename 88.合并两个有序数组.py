#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (49.46%)
# Likes:    801
# Dislikes: 0
# Total Accepted:    285.6K
# Total Submissions: 577.1K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自
# nums2 的元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# nums1.length == m + n
# nums2.length == n
# 0 
# 1 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1
        
        p = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1

        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]
            



# @lc code=end

