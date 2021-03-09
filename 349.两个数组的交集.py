#
# @lc app=leetcode.cn id=349 lang=python
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (70.95%)
# Likes:    309
# Dislikes: 0
# Total Accepted:    150.6K
# Total Submissions: 205K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 
# 
# 示例 2：
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 
# 
# 
# 说明：
# 
# 
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
# 
# 
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        hashtable = {}

        ans = []

        for num in nums1:
            hashtable[num] = 1
        
        for num in nums2:
            if num in hashtable:
                hashtable[num] += 1
                
        for key in hashtable:
            if hashtable[key] > 1:
                ans.append(key)
        
        return ans
            
        
# @lc code=end

